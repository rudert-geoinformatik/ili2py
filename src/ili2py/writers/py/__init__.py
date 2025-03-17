from ili2py.interfaces.interlis.interlis_24.ilismeta16 import ImdTransfer

from ili2py.writers.py.interlis23 import reader_classes


def create_python_classes(transfer: ImdTransfer, output_path: str) -> str:
    # TODO: This is probably ugly (aka can we have mixed ili versions?
    if transfer.datasection.ModelData[-1].Model.iliVersion in ['2.3', '2.4']:
        return reader_classes(transfer, output_path)
    else:
        raise NotImplemented
