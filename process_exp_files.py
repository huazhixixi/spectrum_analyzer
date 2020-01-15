import numpy as np
from PyQt5.QtWidgets import QWidget, QFileDialog, QApplication, QMessageBox
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtCore import QThread

from process_data import read_data
import pyqtgraph


class CalculateSpectrum(QThread):
    calc_finshed = pyqtSignal(np.ndarray, np.ndarray)

    def __init__(self, data, fs, fft_point, window):
        super(CalculateSpectrum, self).__init__()
        self.data = data
        self.fs = fs
        self.fft_point = fft_point
        self.window = window

    def run(self) -> None:
        self.data = np.atleast_2d(self.data)
        pol_number = self.data.shape[0]
        spectrum_sequence = np.zeros((pol_number, int(self.fft_point)), dtype=self.data.dtype)

        from scipy.signal import welch
        for i in range(pol_number):
            f, p = welch(self.data[i], self.fs, window=self.window, nfft=self.fft_point, return_onesided=False,
                         detrend=False)
            spectrum_sequence[i] = p
        spectrum_sequence = 10 * np.log10(np.abs(spectrum_sequence))
        self.calc_finshed.emit(f, spectrum_sequence)


from process_ui import Ui_Widget


class ReadData(QWidget):

    def __init__(self):
        super(ReadData, self).__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.batProcessingButton.clicked[bool].connect(self.bat_processing_csv)
        self.ui.PlotSpectrumButton.clicked[bool].connect(self.plot_spectrum)
        self.ui.openCsvButton.clicked[bool].connect(self.open_csv)
        self.ui.savenpzButton.clicked[bool].connect(self.save_npz)
        self.ui.savematButton.clicked[bool].connect(self.save_mat)



        self.default_dir = None

    @pyqtSlot(bool)
    def bat_processing_csv(self):

        save_dir = self.ui.saveDirLineEdit.text()
        if not(self.ui.isSavematRaido.isChecked()) and not self.ui.isSavenpz.isChecked():
            QMessageBox.warning(None, 'error', 'please chose save format', QMessageBox.Yes)
            return
        if not save_dir:
            QMessageBox.warning(None, 'error', 'please input save dir', QMessageBox.Yes)
            return
        file_names, _ = QFileDialog.getOpenFileNames(self, 'open files', './', 'data (*.csv)')

        if file_names:
            group_number = len(file_names)//4
            if group_number <=0:
                QMessageBox.warning(None,'error','please ensure there exist at least four channels',QMessageBox.Yes)
                return

            for ith_group in range(group_number):
                ch1,ch2,ch3,ch4 = file_names[4*ith_group:4*ith_group+4]
                if self.ui.isSavematRaido.isChecked():
                    read_data(ch1,ch2,ch3,ch4,None,save_dir+'/' + str(ith_group) +'.mat',False)
                if self.ui.isSavenpz.isChecked():
                    read_data(ch1,ch2,ch3,ch4,save_dir +'/' + str(ith_group) +'.npz',None,True)





    @pyqtSlot(bool)
    def plot_spectrum(self):
        pass

    @pyqtSlot(bool)
    def open_csv(self):
        pass

    @pyqtSlot(bool)
    def save_npz(self):
        pass

    @pyqtSlot(bool)
    def save_mat(self):
        pass


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = ReadData()
    window.show()

    sys.exit(app.exec())
