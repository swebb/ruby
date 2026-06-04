class HIRPrinter:
    def __init__(self, val):
        self.val = val

    def to_string(self):
        # return f'iseq: {self.val["iseq"]}\nblocks: {self.val["entry_block"]'
        print(f'self: {self}')
        print(f'iseq: {self.val["iseq"]}')
        # print(f'blocks: {self.val["blocks"]}')
        print(f'isns: {zjit::hir::Insn(self.val["insns"])}')
        # for insn in range(self.val["blocks"].len):
            # print(f'block: {block}')

def register_printers(val):
    return HIRPrinter(val) if str(val.type)=='*mut zjit::hir::Function'\
    else None

# gdb.pretty_printers.append(register_printers)
