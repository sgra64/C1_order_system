"""
Sample order data, each tuple represents an order item
"""
sample_order_items = [
    # order_id, customer_id, stock_id, units_ordered, description
    ("00-784-33313", 862466, "4417B001", 5, "EOS 80D Gehäuse + EF-S 18-55mm f/3.5-5.6 IS STM"),
    ("00-184-40592", 952417, "1575C001", 1, "EOS M50 Gehäuse - Schwarz + EF-M 18-150mm f/3.5-6.3 IS STM Kit"),
    ("00-704-63328", 133295, "2713A001", 3, "EOS 200D Gehäuse - Silber + EF-S 18-55mm f/4-5.6 IS STM - Silber"),
    ("00-505-72315", 892007, "9930B001", 3, "EF 75-300mm f/4-5.6 III"),
    ("00-999-13198", 652251, "0958C037", 4, "EF-S 10-18mm f/4.5-5.6 IS STM + EW 73 + LC Kit"),
    ("00-937-09641", 714268, "2681C002", 1, "EF 135mm f/2L USM "),
    ("00-802-56408", 949365, "1724C022", 3, "EF 400mm f/4 DO IS II USM"),
    ("00-802-56408", 949365, "9930B001", 3, "EF 75-300mm f/4-5.6 III"),
    ("00-559-16396", 877533, "0960C006", 3, "EF-S 10-22mm f/3.5-4.5 USM"),
    ("00-368-74862", 497631, "2680C022", 5, "EF-S 18-200mm f/3.5-5.6 IS "),
    ("00-528-25641", 337318, "2680C064", 1, "EF-S 18-55mm f/4-5.6 IS STM"),
    ("00-558-57092", 902233, "2680C064", 1, "EF-S 18-55mm f/4-5.6 IS STM"),
    ("00-484-85206", 722566, "0959C032", 1, "EF-S 24mm f/2.8 STM"),
    ("00-407-98735", 248966, "4660A001", 1, "Augenkorrekturlinsen EOS Eg mit Augenmuschel Eg 0 Dioptrien"),
    ("00-200-46326", 986973, "5178B005", 1, "WP-DC54"),
    ("00-992-27927", 472033, "0036X207", 3, "XA11"),
    ("00-289-84556", 700281, "2746B005", 3, "NB-5L Akku"),
    ("00-539-82395", 625355, "1276C005", 1, "IFC-400PCU"),
    ("00-729-74333", 827435, "9199A001", 1, "LC-E10"),
    ("00-631-18197", 115666, "2211C049", 3, "MP-E 65mm f/2.8 1-5fach Lupenobjektiv"),
    ("00-594-96628", 386232, "9554B001", 1, "BP-110 OTH Akku"),
    ("00-745-35878", 212921, "6219B006", 1, "E-58II"),
    ("00-992-27927", 472033, "3563B001", 1, "PIXMA MG3650 - Schwarz"),
    ("00-481-11785", 863071, "2588A001", 1, "Remote Controller Adapter RA-E3"),
    ("00-968-15982", 839603, "9530B001", 3, "EH20-L"),
    ("00-146-92306", 520875, "2728C022", 1, "PowerShot G9 X Mark II - Silber"),
    ("00-200-46326", 986973, "5247B003", 4, "CN-E 20mm T1.5 L F (F)"),
    ("00-200-46326", 986973, "1276C005", 1, "IFC-400PCU"),
    ("00-176-64731", 564838, "2438A001", 1, "CN-E 85mm L F (M)"),
    ("00-234-65237", 712039, "1135B001", 2, "CG-A10"),
    ("00-901-10309", 863071, "7277A001", 1, "Li-lon Akku LP-E5"),
    ("00-286-25773", 148409, "1367C066", 1, "Color Filter SCF-E3"),
    ("00-485-04575", 692794, "2494C001", 1, "LP 816"),
    ("00-437-55047", 777553, "4726B003", 3, "LEGRIA HF R88 - Schwarz"),
    ("00-168-88066", 607947, "5743B003", 1, "CN-E 35mm F1.5 L F (M)"),
    ("00-769-34958", 258090, "1751C001", 1, "Lens Case 800"),
    ("00-605-10869", 194021, "2728C022", 1, "PowerShot G9 X Mark II - Silber"),
    ("00-559-16396", 877533, "1751C001", 1, "Lens Case 800"),
    ("00-802-56408", 949365, "2728C022", 1, "PowerShot G9 X Mark II - Silber"),
    ("00-840-58227", 386947, "2213C003", 1, "EW-78E Streulichtblende "),
    ("00-331-40167", 137704, "1367C066", 1, "Color Filter SCF-E3"),
    ("00-605-10869", 194021, "9967B002", 1, "MAXIFY MB2755"),
    ("00-532-44167", 193667, "1806C010", 3, "Selbstwechselbare Laser-Mattscheiben Typ Ef Focusing Screen Ef-D"),
    ("00-109-15056", 559616, "4724B001", 3, "EOS Cinema C100 Mark II + EF 24-105mm f/3.5-5.6 IS STM"),
    ("00-992-27927", 472033, "7277A001", 1, "Li-lon Akku LP-E5"),
    ("00-494-04757", 898815, "0515C026", 1, "Adapter für Gelatine-Filter-Halter TYP WII 52mm"),
    ("00-948-51610", 184336, "0580C001", 1, "EH27-L"),
    ("00-588-47326", 645386, "5108B002", 3, "MAXIFY MB2750 AT"),
    ("00-489-11031", 948339, "0038X888", 1, "XA30 BP-820 Power Kit"),
    ("00-913-26787", 868480, "2218C010", 1, "EW-68A Streulichtblende"),
    ("00-522-29011", 758891, "9532B001", 1, "CANON TEXTILE BAG HOLSTER HL100 BLACK"),
    ("00-554-82798", 193667, "2218C010", 1, "EW-68A Streulichtblende"),
    ("00-239-23627", 652251, "4587B002", 3, "EW-83H Streulichtblende"),
    ("00-423-97519", 193667, "2863A001", 3, "Schutzfilter 82mm"),
    ("00-286-25773", 148409, "8597B002", 1, "EW-83F Streulichtblende "),
    ("00-296-29571", 446428, "1172C001", 1, "BODY JACKET EH29-CJ Black"),
    ("00-354-75629", 356160, "9967B002", 1, "MAXIFY MB2755"),
    ("00-804-50065", 862466, "7277A001", 5, "Li-lon Akku LP-E5"),
    ("00-896-56165", 998759, "0581C009", 5, "CB-2LXE Akkuladegerät"),
    ("00-925-64717", 915658, "0580C001", 1, "EH27-L"),
    ("00-691-20558", 739314, "9532B001", 1, "CANON TEXTILE BAG HOLSTER HL100 BLACK"),
    ("00-882-85740", 654319, "7276A001", 1, "DR-E12 DC Kuppler"),
    ("00-149-63454", 423215, "2713A001", 1, "EOS 200D Gehäuse - Silber + EF-S 18-55mm f/4-5.6 IS STM - Silber"),
    ("00-545-67952", 176698, "0971C026", 1, "500D (58mm) Nahlinse, mehrgliedriger Achromat"),
    ("00-527-85861", 489802, "4660A001", 1, "Augenkorrekturlinsen EOS Eg mit Augenmuschel Eg 0 Dioptrien"),
    ("00-933-44898", 524236, "4728B001", 2, "BP-718"),
    ("00-592-00442", 975627, "6319B001", 4, "BG-E14"),
    ("00-593-27507", 238239, "9841B001", 1, "EOS Cinema C300 EF DAF"),
    ("00-802-93399", 400345, "1883C001", 3, "PIXMA TR7550 - Schwarz"),
    ("00-173-92484", 557526, "0579C001", 2, "BG-E13"),
    ("00-605-10869", 194021, "4426B005", 1, "Silicone Jacket SJ-DC1"),
    ("00-829-28711", 710171, "2300C001", 1, "SS-600 Schultergurt"),
    ("00-453-50189", 765422, "2713A001", 3, "EOS 200D Gehäuse - Silber + EF-S 18-55mm f/4-5.6 IS STM - Silber"),
    ("00-145-93401", 737397, "0971C026", 1, "500D (58mm) Nahlinse, mehrgliedriger Achromat"),
    ("00-881-07292", 331712, "2187B001", 1, "EOS 4000D Gehäuse + EF-S 18-55mm f/3.5-5.6 III Value Up Kit"),
    ("00-746-01844", 596378, "2438A001", 1, "CN-E 85mm L F (M)"),
    ("00-222-54933", 156290, "9447A001", 1, "Augenkorrekturlinsen EOS Eg mit Augenmuschel Eg +3 Dioptrien"),
    ("00-546-74194", 539694, "5743B003", 1, "CN-E 35mm F1.5 L F (M)"),
    ("00-728-96604", 813951, "1729C001", 1, "TS-E 135mm f/4L Macro"),
    ("00-546-05543", 640924, "2599A001", 1, "Selbstwechselbare Laser-Mattscheibe Typ Ec Einsatz Ec-C IV"),
    ("00-626-06625", 519786, "1896B003", 2, "ND 4-L 72MM Filter"),
    ("00-379-67889", 722566, "1575C001", 1, "EOS M50 Gehäuse - Schwarz + EF-M 18-150mm f/3.5-6.3 IS STM Kit"),
    ("00-486-28187", 954424, "9967B002", 1, "MAXIFY MB2755"),
    ("00-835-19329", 400345, "9530B001", 1, "EH20-L"),
    ("00-919-29082", 736626, "2649A001", 1, "Augenkorrekturlinsen EOS Eg mit Augenmuschel Eg +1 Dioptrien"),
    ("00-348-56578", 611425, "9199A001", 1, "LC-E10"),
    ("00-403-51403", 769540, "0972B002", 3, "EW-83J Streulichtblende"),
    ("00-554-35346", 777553, "2713A001", 1, "EOS 200D Gehäuse - Silber + EF-S 18-55mm f/4-5.6 IS STM - Silber"),
    ("00-942-80970", 356160, "9838B003", 2, "LEGRIA HF R806 - Weiß Essential Kit"),
    ("00-280-08736", 795352, "7276A001", 1, "DR-E12 DC Kuppler"),
    ("00-461-38412", 736626, "2675A001", 3, "CANON TEXTILE BAG MS10"),
    ("00-152-51515", 512746, "0960C037", 4, "250D (58mm) Nahlinse, mehrgliedriger Achromat"),
    ("00-301-39012", 829951, "0038X888", 1, "XA30 BP-820 Power Kit"),
    ("00-493-67312", 201559, "4042B001", 1, "TL-H58"),
    ("00-351-97973", 615916, "2297B005", 6, "MLA-DC1 Macro Light Adapter"),
    ("00-609-44671", 368075, "1954B001", 5, "Selbstwechselbare Laser-Mattscheibe Typ Ec Einsatz Ec-C6"),
    ("00-108-57758", 596378, "2649A001", 1, "Augenkorrekturlinsen EOS Eg mit Augenmuschel Eg +1 Dioptrien"),
    ("00-494-29092", 559616, "2300C001", 1, "SS-600 Schultergurt"),
    ("00-829-28711", 710171, "0580C001", 1, "EH27-L"),
    ("00-695-62478", 661165, "8326B002", 1, "ES-52 Streulichtblende "),
    ("00-346-36816", 331712, "4771B001", 1, "EOS 4000D Gehäuse"),
    ("00-605-10869", 194021, "0042X095", 1, "XA15"),
    ("00-829-28711", 710171, "8747B006", 5, "E-73"),
    ("00-845-53920", 199929, "2588A001", 1, "Remote Controller Adapter RA-E3"),
    ("00-557-86461", 527327, "1172C001", 1, "BODY JACKET EH29-CJ Black"),
    ("00-290-15219", 868480, "5752B003", 3, "MAXIFY MB 5450 AT"),
    ("00-605-10869", 194021, "6219B006", 1, "E-58II"),
    ("00-200-46326", 986973, "2599A001", 1, "Selbstwechselbare Laser-Mattscheibe Typ Ec Einsatz Ec-C IV"),
    ("00-229-85237", 677560, "9763A001", 5, "CG-800"),
    ("00-879-31242", 645386, "6472A012", 1, "TC-DC58E Telekonverter"),
    ("00-933-90876", 127234, "9526B005", 1, "Timer TC-80 N 3"),
    ("00-449-84441", 607947, "3349B001", 1, "MAXIFY MB2155 AT"),
    ("00-415-31208", 640924, "2882A001", 3, "NB-CP2LH Akku"),
    ("00-660-87526", 939503, "7276A001", 1, "DR-E12 DC Kuppler"),
    ("00-747-27329", 892007, "0886C001", 1, "LP 1222"),
    ("00-528-25641", 337318, "0515C026", 1, "Adapter für Gelatine-Filter-Halter TYP WII 52mm"),
    ("00-801-18144", 902233, "1759C001", 1, "PIXMA TS3150 - Schwarz"),
    ("00-691-20558", 739314, "6472A012", 1, "TC-DC58E Telekonverter"),
    ("00-594-28331", 861540, "2388A001", 1, "CN-E 50mm L F (M)"),
    ("00-130-90950", 896469, "0042X095", 1, "XA15"),
    ("00-263-81869", 561350, "2187B001", 1, "EOS 4000D Gehäuse + EF-S 18-55mm f/3.5-5.6 III Value Up Kit"),
    ("00-626-06625", 519786, "4724B001", 3, "EOS Cinema C100 Mark II + EF 24-105mm f/3.5-5.6 IS STM"),
    ("00-559-16396", 877533, "2494C001", 1, "LP 816"),
    ("00-564-57334", 193667, "8597B002", 1, "EW-83F Streulichtblende "),
    ("00-559-16396", 877533, "9554B001", 1, "BP-110 OTH Akku"),
    ("00-219-30989", 939503, "0886C001", 1, "LP 1222"),
    ("00-444-44157", 825647, "2654A001", 2, "Augenkorrekturlinsen EOS E ohne Augenmuschel + 1 Dioptrie"),
    ("00-589-21455", 640667, "0251C001", 3, "CAMERA FACE JACKET EH28-FJ HZ"),
    ("00-296-27225", 832681, "2540A011", 4, "DCC-2400"),
    ("00-933-90876", 127234, "9530B001", 1, "EH20-L"),
    ("00-305-98057", 652251, "3349B001", 1, "MAXIFY MB2155 AT"),
    ("00-210-52970", 258090, "3011C013", 3, "ACK-DC110 Netzadapter"),
    ("00-847-68782", 861618, "9553B001", 1, "BP-A30"),
    ("00-303-16529", 143871, "6569B001", 1, "ES-79 II Streulichtblende"),
    ("00-709-44845", 839603, "5743B003", 1, "CN-E 35mm F1.5 L F (M)"),
    ("00-433-64844", 527327, "6569B001", 1, "ES-79 II Streulichtblende"),
    ("00-621-07588", 266388, "3165V706", 6, "LP 1224"),
    ("00-444-30093", 915658, "6323B001", 3, "EOS 4000D Gehäuse + EF-S 18-55mm f/3.5-5.6 III Kit"),
    ("00-407-98735", 248966, "9838B003", 3, "LEGRIA HF R806 - Weiß Essential Kit"),
    ("00-761-56756", 737397, "4426B005", 3, "Silicone Jacket SJ-DC1"),
    ("00-976-26476", 661165, "2588A001", 1, "Remote Controller Adapter RA-E3"),
    ("00-435-55131", 948339, "5124B005", 3, "NB4-300 Akku"),
    ("00-425-45852", 386947, "9843B001", 3, "BP-A60"),
    ("00-626-06625", 519786, "7276A001", 1, "DR-E12 DC Kuppler"),
    ("00-199-34355", 896469, "1485C001", 1, "EOS M100 Gehäuse - Schwarz + EF-M 15-45mm f/3.5-6.3 IS STM + EF-M 22mm f/2 STM Kit"),
    ("00-542-28910", 827435, "5178B005", 1, "WP-DC54"),
    ("00-208-87527", 167361, "0042X095", 1, "XA15")
]
