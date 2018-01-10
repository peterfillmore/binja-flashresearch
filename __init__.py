import struct
import traceback

#from binaryninja import Architecture, BinaryView, SegmentFlag, log_error, enums, types
from binaryninja import *
#2251-68-5
#entry_addr = 0x4000
#2303
entry_addr = 0x0

class FlashDriveView(BinaryView):
    name = "FlashDrive"
    long_name = "FlashDrive Memory Dump"
    
    def __init__(self, data):
        BinaryView.__init__(self, file_metadata=data.file, parent_view=data)
        self.raw = data

    @classmethod
    def is_valid_for_data(self, data):
        if data[0:8] == "BtPramCd":
            return True
        else:
            return False

    def init(self):
        try:
            self.platform = Architecture['i8051'].standalone_platform
            self.arch = Architecture['i8051']
            
            self.entry_addr = entry_addr #identified location of main
            #self.entry_addr = 0x0000 #identified location of main
            self.add_entry_point(self.entry_addr)
            #DATA section 
            
            self.add_auto_segment(0x0000, 0x0080, 0x0, 0x0,SegmentFlag.SegmentReadable | SegmentFlag.SegmentExecutable | SegmentFlag.SegmentWritable) 
            #IDATA section 
            
            self.add_auto_segment(0x0080, 0x0080, 0x0, 0x0,SegmentFlag.SegmentReadable | SegmentFlag.SegmentExecutable | SegmentFlag.SegmentWritable) 
            
            self.add_auto_segment(0x0080, 0x4000-0x80, 0x0, 0x0,SegmentFlag.SegmentReadable | SegmentFlag.SegmentExecutable | SegmentFlag.SegmentWritable) 
            #code 
            #self.add_auto_segment(0x0000, 0xFFFF, 0x0, 0x0,SegmentFlag.SegmentReadable | SegmentFlag.SegmentExecutable | SegmentFlag.SegmentWritable) 
            #2303 
            self.add_auto_segment(0x0000, 0xFFFF, 0x200, len(self.raw) - 0x200,SegmentFlag.SegmentReadable | SegmentFlag.SegmentExecutable | SegmentFlag.SegmentWritable)
            #2258-68-5
            #self.add_auto_segment(0x4000, 0xFFFF, 0x200, 0xFFFF,SegmentFlag.SegmentReadable | SegmentFlag.SegmentExecutable | SegmentFlag.SegmentWritable)
           
            #define registers
            #bank 0 
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x00, "R0"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x01, "R1"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x02, "R2"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x03, "R3"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x04, "R4"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x05, "R5"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x06, "R6"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x07, "R7"))
            #bank 1 
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x08, "R0"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x09, "R1"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x0a, "R2"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x0b, "R3"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x0c, "R4"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x0d, "R5"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x0e, "R6"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x0f, "R7"))
            #bank 2 
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x10, "R0"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x11, "R1"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x12, "R2"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x13, "R3"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x14, "R4"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x15, "R5"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x16, "R6"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x17, "R7"))
            #bank 3 
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x18, "R0"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x19, "R1"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x1a, "R2"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x1b, "R3"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x1c, "R4"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x1d, "R5"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x1e, "R6"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x1f, "R7"))

            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x80, "P0"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x90, "P1"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0xA0, "P2"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0xB0, "P3"))
            
            #DEFINE SFRs    
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0xe0, "A"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0xf0, "B"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0xd0, "PSW"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x81, "SP"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x82, "DPL"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x83, "DPH"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x87, "PCON"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x88, "TCON"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x89, "TMOD"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x8A, "TL0"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x8B, "TL1"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x8C, "TH0"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x8D, "TH1"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0xA8, "IE"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0xB8, "IP"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x98, "SCON"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0x99, "SBUF"))
            #define ports
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0xF000, "REGBANK"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0xF14C, "GPIO0OUT"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0xF14D, "GPIO0DIR"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0xF14E, "GPIO1OUT"))
            self.define_auto_symbol(types.Symbol(enums.SymbolType.DataSymbol, 0xF14F, "GPIO1OUT"))

            #define functions
            self.add_function(entry_addr + 0x0)
            self.define_auto_symbol(types.Symbol(enums.SymbolType.FunctionSymbol, entry_addr + 0x0, "_RESET"))
            self.add_function(entry_addr + 0x3)
            self.define_auto_symbol(types.Symbol(enums.SymbolType.FunctionSymbol, entry_addr + 0x3, "IE0"))
            self.add_function(entry_addr + 0xB)
            self.define_auto_symbol(types.Symbol(enums.SymbolType.FunctionSymbol, entry_addr + 0xB, "TF0"))
            self.add_function(entry_addr + 0x13)
            self.define_auto_symbol(types.Symbol(enums.SymbolType.FunctionSymbol, entry_addr + 0x13, "IE1"))
            self.add_function(entry_addr + 0x1B)
            self.define_auto_symbol(types.Symbol(enums.SymbolType.FunctionSymbol, entry_addr + 0x1B, "TF0"))
            self.add_function(entry_addr + 0x1B)
            self.define_auto_symbol(types.Symbol(enums.SymbolType.FunctionSymbol, entry_addr + 0x23, "SERIAL0"))
            self.add_function(entry_addr + 0x23)
            self.define_auto_symbol(types.Symbol(enums.SymbolType.FunctionSymbol, entry_addr + 0x2B, "TF2_EXF2"))
            self.add_function(entry_addr + 0x2B)
            #self.define_auto_symbol(types.Symbol(enums.SymbolType.FunctionSymbol, entry_addr + 0x2B, "TF"))
            
            nandreg_struct = types.Structure()
            nandreg_struct.append(types.Type.int(1, sign=False), 'r0')
            self.define_type(Type.generate_auto_type_id("source", "nandreg"), "nandreg", Type.structure_type(nandreg_struct))
            #log_warn("platform types={}".format(dir(self.platform.types))) 
            #self.platform.types.update({'nandreg': Type.structure_type[nandreg1_struct]}) 
            #create structures
            #log_warn("platform types={}".format(self.platform.types)) 

        except:
            log_error(traceback.format_exc())
            return False
        return True

    def perform_is_executable(self):
        return True

    def perform_get_entry_point(self):
        return self.entry_addr

        

FlashDriveView.register()

#FlashDriveView.register_platform_types()
def register_structs():
    nandreg_struct = types.Structure()
    nandreg_struct.append(types.Type.int(1, sign=False), 'raw_cmd')
    nandreg_struct.append(types.Type.array(types.Type.int(1, sign=False), 3), 'u1')
    nandreg_struct.append(types.Type.int(1, sign=False), 'raw_addr')
    nandreg_struct.append(types.Type.array(types.Type.int(1, sign=False), 3), 'u5')
    nandreg_struct.append(types.Type.int(1, sign=False), 'r9')
    nandreg_struct.append(types.Type.array(types.Type.int(1, sign=False), 2), 'uA')
    nandreg_struct.append(types.Type.int(1, sign=False), 'rC')
    nandreg_struct.append(types.Type.array(types.Type.int(1, sign=False), 3), 'uD')
    nandreg_struct.append(types.Type.int(1, sign=False), 'r10')
    nandreg_struct.append(types.Type.array(types.Type.int(1, sign=False), 7), 'u11')
    nandreg_struct.append(types.Type.int(1, sign=False), 'r18')
    nandreg_struct.append(types.Type.array(types.Type.int(1, sign=False), 5), 'u19')
    nandreg_struct.append(types.Type.int(1, sign=False), 'status')
    nandreg_struct.append(types.Type.array(types.Type.int(1, sign=False), 0x19), 'u1F')
    nandreg_struct.append(types.Type.int(1, sign=False), 'r38')
    nandreg_struct.append(types.Type.int(1, sign=False), 'r39')
    nandreg_struct.append(types.Type.int(1, sign=False), 'rA')
    nandreg_struct.append(types.Type.int(1, sign=False), 'rB')
    nandreg_struct.append(types.Type.int(1, sign=False), 'rC')
    nandreg_struct.append(types.Type.int(1, sign=False), 'rD')
    nandreg_struct.append(types.Type.array(types.Type.int(1, sign=False), 2), 'rE')
    nandreg_struct.append(types.Type.int(1, sign=False), 'r40')
    nandreg_struct.append(types.Type.int(1, sign=False), 'dmasize')
    nandreg_struct.append(types.Type.int(1, sign=False), 'r42')
    nandreg_struct.append(types.Type.int(1, sign=False), 'dma_mode')
    nandreg_struct.append(types.Type.array(types.Type.int(1, sign=False), 3), 'u44')
    nandreg_struct.append(types.Type.int(1, sign=False), 'r47')
    nandreg_struct.append(types.Type.array(types.Type.int(1, sign=False), 0x14), 'u48')
    nandreg_struct.append(types.Type.int(1, sign=False), 'r5C')
    nandreg_struct.append(types.Type.int(1, sign=False), 'dma_cmd')
    nandreg_struct.append(types.Type.array(types.Type.int(1, sign=False), 0x0B), 'u61')
    nandreg_struct.append(types.Type.int(1, sign=False), 'dma1_page')
    nandreg_struct.append(types.Type.array(types.Type.int(1, sign=False), 0x03), 'u6D')
    nandreg_struct.append(types.Type.int(1, sign=False), 'dma0_page')
    nandreg_struct.append(types.Type.array(types.Type.int(1, sign=False), 0x03), 'u71')
    nandreg_struct.append(types.Type.int(1, sign=False), 'dma1_ptr0')
    nandreg_struct.append(types.Type.int(1, sign=False), 'dma1_ptr1')
    nandreg_struct.append(types.Type.int(1, sign=False), 'dma1_ptr2')
    nandreg_struct.append(types.Type.int(1, sign=False), 'dma1_ptr3')
    nandreg_struct.append(types.Type.int(1, sign=False), 'dma0_ptr0')
    nandreg_struct.append(types.Type.int(1, sign=False), 'dma0_ptr1')
    nandreg_struct.append(types.Type.int(1, sign=False), 'dma0_ptr2')
    nandreg_struct.append(types.Type.int(1, sign=False), 'dma0_ptr3')
    nandreg_struct.append(types.Type.array(types.Type.int(1, sign=False), 4), 'u7C')
    nandreg_struct.append(types.Type.int(1, sign=False), 'r80')
    nandreg_struct.append(types.Type.array(types.Type.int(1, sign=False), 0x1B), 'u81')
    nandreg_struct.append(types.Type.int(1, sign=False), 'page_size_l')
    nandreg_struct.append(types.Type.int(1, sign=False), 'page_size_h')
    nandreg_struct.append(types.Type.int(1, sign=False), 'r9E')
    nandreg_struct.append(types.Type.int(1, sign=False), 'r9F')
    nandreg_struct.append(types.Type.array(types.Type.int(1, sign=False), 0x4C), 'uA0')
    nandreg_struct.append(types.Type.int(1, sign=False), 'rEC')
    nandreg_struct.append(types.Type.array(types.Type.int(1, sign=False), 0x13), 'uED')
    
    #typedef struct
    #{
    #    BYTE        r0,r1,r2,r3,r4;
    #    BYTE        ptr_l, ptr_m, ptr_h; //buffer ptr = buf_pa>>8
    #    BYTE        r8,r9;
    #    BYTE        ofs; // buffer offset, data addr will be ptr<<8 + ofs*0x200
    #    BYTE        rB;
    #    BYTE        len_l, len_m, len_h; //C,D,E
    #    BYTE        rF,r10,r11,r12;
    #    BYTE        cs; //13
    #    BYTE        r14,r15,r16,r17,r18,r19;
    #    BYTE        fifo_count;
    #    BYTE        r1B;
    #    BYTE        fifo; //1C
    #} EPREGS;
    EPREGS_struct = types.Structure()
    EPREGS_struct.append(types.Type.int(1, sign=False), 'r0')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'r1')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'r2')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'r3')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'ptr_l')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'ptr_m')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'ptr_h')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'r8')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'r9')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'ofs')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'rB')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'len_l')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'len_m')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'len_h')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'rF')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'r10')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'r11')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'r12')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'cs')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'r14')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'r15')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'r16')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'r17')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'r18')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'r19')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'fifo_count')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'r1B')
    EPREGS_struct.append(types.Type.int(1, sign=False), 'fifo')
    
    #self.define_type(Type.generate_auto_type_id("source", "NANDREG"), "NANDREG", Type.structure_type(nandreg_struct))
    #self.define_user_type("NANDREG", Type.structure_type(nandreg_struct))
    #self.define_type(Type.generate_auto_type_id("source", "NFC1"), "NFC1", Type.structure_type(nandreg_struct))
    #
    #self.define_type(Type.generate_auto_type_id("source", "EPREGS"), "EPREGS", Type.structure_type(EPREGS_struct))
    #self.define_type(Type.generate_auto_type_id("source", "EP1"), "EP1", Type.structure_type(EPREGS_struct))
    #self.define_type(Type.generate_auto_type_id("source", "EP2"), "EP2", Type.structure_type(EPREGS_struct))
    #self.define_type(Type.generate_auto_type_id("source", "EP3"), "EP3", Type.structure_type(EPREGS_struct))
    #self.define_type(Type.generate_auto_type_id("source", "EP4"), "EP4", Type.structure_type(EPREGS_struct))

