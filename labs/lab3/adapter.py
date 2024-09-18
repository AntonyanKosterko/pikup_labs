class OldPrinter:
    def print_old(self, message: str):
        return f"OldPrinter: {message}"

class PrinterAdapter:
    def __init__(self, old_printer: OldPrinter):
        self.old_printer = old_printer

    def print(self, message: str):
        return self.old_printer.print_old(message)

if __name__ == "__main__":
    old_printer = OldPrinter()
    printer_adapter = PrinterAdapter(old_printer)
    
    print(printer_adapter.print("Hello"))
