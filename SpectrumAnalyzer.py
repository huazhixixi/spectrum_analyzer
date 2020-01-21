from PyQt5.QtWidgets import QWidget
from SpectrunUi import Ui_Form
from PyQt5.QtWidgets import QApplication,QFileDialog,QMessageBox
from PyQt5.QtCore import pyqtSlot,QThread,pyqtSignal
import numpy as np
import pyqtgraph as pg
class CalculateSpectrum(QThread):

    calc_finshed = pyqtSignal(np.ndarray,np.ndarray)

    def __init__(self,data,fs,fft_point,window):
        super(CalculateSpectrum, self).__init__()
        self.data = data
        self.fs = fs
        self.fft_point = fft_point
        self.window = window


    def run(self) -> None:

        self.data = np.atleast_2d(self.data)
        pol_number = self.data.shape[0]
        spectrum_sequence = np.zeros((pol_number,int(self.fft_point)),dtype=self.data.dtype)

        from scipy.signal import welch
        for i in range(pol_number):
            f,p = welch(self.data[i], self.fs, window=self.window,nfft=self.fft_point,return_onesided=False,detrend=False)
            spectrum_sequence[i] = p
        spectrum_sequence = 10*np.log10(np.abs(spectrum_sequence))
        self.calc_finshed.emit(f,spectrum_sequence)

class SpectrumAnalyzer(QWidget):
    def __init__(self,parent=None):
        super(SpectrumAnalyzer, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.data = None
        self.ui.AnalyzeButton.clicked[bool].connect(self.analyze_spectrum)

        self.analyzer = None

    @pyqtSlot(bool)
    def analyze_spectrum(self,is_clicked):
        try:

            fs = float(self.ui.fs.text())

            fft_point = float(self.ui.FFTPoint.text())
            self.chidu = self.ui.Ychidu.currentText().lower()
        except Exception as e:
            QMessageBox.warning(None,'error',str(e),QMessageBox.Yes)
            return
        if self.data is None:
            QMessageBox.warning(None, 'error', 'please read datasamples first', QMessageBox.Yes)
            return


        self.analyzer = CalculateSpectrum(self.data, fs, fft_point, window='hann')
        self.analyzer.calc_finshed.connect(self.plot_spectrum)
        self.analyzer.start()

    @pyqtSlot(np.ndarray,np.ndarray)
    def plot_spectrum(self,f,spectrum):
        f = np.atleast_2d(f)
        spectrum = np.atleast_2d(spectrum)
        f = f[0]
        self.ui.graphicsView.clear()

        if self.chidu =='linear':
            spectrum = 10**(spectrum/10)
        elif self.chidu =='log':
            pass

        for i in range(spectrum.shape[0]):
            w1 = self.ui.graphicsView.addPlot()
            w1.plot(f,spectrum[i],pen=pg.mkPen('r', width=3))
            self.ui.graphicsView.nextRow()

        self.analyzer = None

    @pyqtSlot(bool)
    def on_OpenFileButton_clicked(self,is_clicked):
        # print('xixi')
        fname,_ = QFileDialog.getOpenFileName(self,'open files','./','data (*.npz *.mat)')
        try:
            if fname.endswith('.npz'):
                self.data = np.load(fname)['arr_0']

            if fname.endswith('.mat'):
                from scipy.io import loadmat
                self.data = loadmat(fname)['samples']
        except Exception as e:
            QMessageBox.warning(None, 'error', 'open file error'+str(e), QMessageBox.Yes)
        try:
            self.data = np.atleast_2d(self.data)[:,:2**16]
        except Exception as e:
            self.data = None
            QMessageBox.warning(None, 'error', str(e), QMessageBox.Yes)
            return

        QMessageBox.information(None,'Successful','Read files sccessful',QMessageBox.Yes)


    @pyqtSlot(bool)
    def on_ClearFig_clicked(self, is_clicked):
        self.ui.graphicsView.clear()



def main():
    import sys
    app = QApplication(sys.argv)
    analyzer = SpectrumAnalyzer()
    analyzer.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()

