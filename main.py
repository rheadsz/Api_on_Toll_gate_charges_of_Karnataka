from flask import Flask,jsonify,request

app = Flask(__name__)

tollsm=[
        {
           "Toll Gate Name": "Guilalu",
           "national_highway_id":"48",
           "Charges": "Monthly",
           "Car/Jeep/Van": "2190",
           "LCV": "3540",
           "2 Axle Bus, Truck": "7420",
           "3 Axle Bus, Truck": "11635",
           "4,5,6 Axle Bus, Truck": "11635",
           "7 Axle Bus, Truck": "14165",
           "Heavy Vehicle": "11635"
           },
        {
            "Toll Gate Name": "Bagepalli",
            "national_highway_id":"7",
            "Charges": "Monthly",
            "Car/Jeep/Van": "3070.00",
            "LCV": "4960.00",
            "2 Axle Bus, Truck": "10395.00",
            "3 Axle Bus, Truck": "11340.00",
            "4,5,6 Axle Bus, Truck": "16300.00",
            "7 Axle Bus, Truck": "19845.00",
            "Heavy Vehicle": "16300.00",
            },
        {
            "Toll Gate Name": "Bankapur",
            "national_highway_id":"4",
            "Charges": "Monthly",
            "Car/Jeep/Van": "2165",
            "LCV": "3790",
            "2 Axle Bus, Truck": "7575",
            "3 Axle Bus, Truck": "12175",
            "4,5,6 Axle Bus, Truck": "12175",
            "7 Axle Bus, Truck": "12175",
            "Heavy Vehicle": "12175"
             },
        {   
            "Toll Gate Name": "Brahamarakotlu",
            "national_highway_id":"73",
            "Charges": "Monthly",
            "Car/Jeep/Van": "835",
            "LCV": "1350",
            "2 Axle Bus, Truck": "2825",
            "3 Axle Bus, Truck": "3080",
            "4,5,6 Axle Bus, Truck": "4430",
            "7 Axle Bus, Truck": "5390",
            "Heavy Vehicle": "4430"
               },
           {
                "Toll Gate Name": "Chalageri",
                "national_highway_id":"4",
                "Charges": "Monthly",
                "Car/Jeep/Van": "2545",
                "LCV": "4110",
                "2 Axle Bus, Truck": "8615",
                "3 Axle Bus, Truck": "9395",
                "4,5,6 Axle Bus, Truck": "13510",
                "7 Axle Bus, Truck": "16445",
                "Heavy Vehicle": "18010"
               },
           {
            "Toll Gate Name": "Doddakarenahalli (Neelmangala)",
            "national_highway_id":"75",
            "Charges": "Monthly",
            "Car/Jeep/Van": "1260",
            "LCV": "2200",
            "2 Axle Bus, Truck": "4400",
            "3 Axle Bus, Truck": "7075",
            "4,5,6 Axle Bus, Truck": "7075",
            "7 Axle Bus, Truck": "7075",
            "Heavy Vehicle": "7075"       },
            {
            "Toll Gate Name": "Gaddurur",
            "national_highway_id":"75",
            "Charges": "Monthly",
            "Car/Jeep/Van": "855",
            "LCV": "1380",
            "2 Axle Bus, Truck": "2890",
            "3 Axle Bus, Truck": "3150",
            "4,5,6 Axle Bus, Truck": "4530",
            "7 Axle Bus, Truck": "5515",
            "Heavy Vehicle": "4530"      },
            {
            "Toll Gate Name": "Gundmi",
            "national_highway_id":"66",
            "Charges": "Monthly",
            "Car/Jeep/Van": "1450",
            "LCV": "2345",
            "2 Axle Bus, Truck": "4910",
            "3 Axle Bus, Truck": "7700",
            "4,5,6 Axle Bus, Truck": "7700",
            "7 Axle Bus, Truck": "9375",
            "Heavy Vehicle": "7700"
            },
            {
            "Toll Gate Name": "Hattargi",
            "national_highway_id":"4",
            "Charges": "Monthly",
            "Car/Jeep/Van": "915",
            "LCV": "1475",
            "2 Axle Bus, Truck": "3090",
            "3 Axle Bus, Truck": "3370",
            "4,5,6 Axle Bus, Truck": "4845",
            "7 Axle Bus, Truck": "5900",
            "Heavy Vehicle": "4845"
                    },
            {
            "Toll Gate Name": "Surathkal",
            "national_highway_id":"66",
            "Charges": "Monthly",
            "Car/Jeep/Van": "1740",
            "LCV": "2810",
            "2 Axle Bus, Truck": "5885",
            "3 Axle Bus, Truck": "6420",
            "4,5,6 Axle Bus, Truck": "9225",
            "7 Axle Bus, Truck": "11230",
            "Heavy Vehicle": "9225"
                    },
            {
            "Toll Gate Name": "Talapady",
            "national_highway_id":"66",
            "Charges": "Monthly",
            "Car/Jeep/Van": "1305",
            "LCV": "2015",
            "2 Axle Bus, Truck": "4100",
            "3 Axle Bus, Truck": "6230",
            "4,5,6 Axle Bus, Truck": "6230",
            "7 Axle Bus, Truck": "8050",
            "Heavy Vehicle": "6230"
                    }
            ]
tollsd=[
        {
            "Toll Gate Name": "Bagepalli",
            "national_highway_id":"7",
            "Charges": "Single",
            "Car/Jeep/Van": "90",
            "LCV": "150",
            "2 Axle Bus, Truck": "310",
            "3 Axle Bus, Truck": "340",
            "4,5,6 Axle Bus, Truck": "490",
            "7 Axle Bus, Truck": "595",
            "Heavy Vehicle": "490"  
            },
        {    
             "Toll Gate Name": "Guilalu",
             "national_highway_id":"48",
             "Charges": "Single",
             "Car/Jeep/Van": "65",
             "LCV": "105",
             "2 Axle Bus, Truck": "225",
             "3 Axle Bus, Truck": "350",
             "4,5,6 Axle Bus, Truck": "350",
             "7 Axle Bus, Truck": "425",
             "Heavy Vehicle": "350"
                },
            
        {   
            "Toll Gate Name": "Bankapur",
            "national_highway_id":"4",
            "Charges": "Single",
            "Car/Jeep/Van": "70",
            "LCV": "125",
            "2 Axle Bus, Truck": "255",
            "3 Axle Bus, Truck": "405",
            "4,5,6 Axle Bus, Truck": "405",
            "7 Axle Bus, Truck": "405",
            "Heavy Vehicle": "405"},
        {   
            "Toll Gate Name": "Brahamarakotlu",
            "national_highway_id":"73",
            "Charges": "Single",
            "Car/Jeep/Van": "25",
            "LCV": "40",
            "2 Axle Bus, Truck": "85",
            "3 Axle Bus, Truck": "90",
            "4,5,6 Axle Bus, Truck": "135",
            "7 Axle Bus, Truck": "160",
            "Heavy Vehicle": "135"},
        {   
            "Toll Gate Name": "Chalageri",
            "national_highway_id":"4",
            "Charges": "Single",
            "Car/Jeep/Van": "75",
            "LCV": "125",
            "2 Axle Bus, Truck": "260",
            "3 Axle Bus, Truck": "280",
            "4,5,6 Axle Bus, Truck": "405",
            "7 Axle Bus, Truck": "495",
            "Heavy Vehicle": "545"},
        {   
            "Toll Gate Name": "Doddakarenahalli (Neelmangala)",
            "national_highway_id":"75",
            "Charges": "Single",
            "Car/Jeep/Van": "40",
            "LCV": "75",
            "2 Axle Bus, Truck": "145",
            "3 Axle Bus, Truck": "235",
            "4,5,6 Axle Bus, Truck": "235",
            "7 Axle Bus, Truck": "235",
            "Heavy Vehicle": "235"},
        {   
            "Toll Gate Name": "Gaddurur",
            "national_highway_id":"75",
            "Charges": "Single",
            "Car/Jeep/Van": "25",
            "LCV": "40",
            "2 Axle Bus, Truck": "85",
            "3 Axle Bus, Truck": "95",
            "4,5,6 Axle Bus, Truck": "135",
            "7 Axle Bus, Truck": "165",
            "Heavy Vehicle": "135"},
        {
            "Toll Gate Name": "Gundmi",
            "national_highway_id":"66",
            "Charges": "Single",
            "Car/Jeep/Van": "45",
            "LCV": "70",
            "2 Axle Bus, Truck": "145",
            "3 Axle Bus, Truck": "230",
            "4,5,6 Axle Bus, Truck": "230",
            "7 Axle Bus, Truck": "280",
            "Heavy Vehicle": "230"},
        {   
            "Toll Gate Name": "Hattargi",
            "national_highway_id":"4",
            "Charges": "Single",
            "Car/Jeep/Van": "25",
            "LCV": "45",
            "2 Axle Bus, Truck": "95",
            "3 Axle Bus, Truck": "100",
            "4,5,6 Axle Bus, Truck": "145",
            "7 Axle Bus, Truck": "175",
            "Heavy Vehicle": "145"},
        {
            "Toll Gate Name": "Surathkal",
            "national_highway_id":"66",
            "Charges": "Single",
            "Car/Jeep/Van": "50",
            "LCV": "85",
            "2 Axle Bus, Truck": "175",
            "3 Axle Bus, Truck": "195",
            "4,5,6 Axle Bus, Truck": "275",
            "7 Axle Bus, Truck": "335",
            "Heavy Vehicle": "275"},
        {
            "Toll Gate Name": "Talapady",
            "national_highway_id":"66",
            "Charges": "Single",
            "Car/Jeep/Van": "40",
            "LCV": "60",
            "2 Axle Bus, Truck": "125",
            "3 Axle Bus, Truck": "185",
            "4,5,6 Axle Bus, Truck": "185",
            "7 Axle Bus, Truck": "240",
            "Heavy Vehicle": "185"}
                 
            ]
tollsr=[
    {
        "Toll Gate Name": "Bagepalli",
        "national_highway_id":"7",
        "Charges": "Return",
        "Car/Jeep/Van": "140",
        "LCV": "225",
        "2 Axle Bus, Truck": "470",
        "3 Axle Bus, Truck": "510",
        "4,5,6 Axle Bus, Truck": "735",
        "7 Axle Bus, Truck": "895",
        "Heavy Vehicle": "735"},
    {   
        "Toll Gate Name": "Guilalu",
        "national_highway_id":"48",
        "Charges": "Return",
        "Car/Jeep/Van": "100",
        "LCV": "160",
        "2 Axle Bus, Truck": "335",
        "3 Axle Bus, Truck": "525",
        "4,5,6 Axle Bus, Truck": "525",
        "7 Axle Bus, Truck": "635",
        "Heavy Vehicle": "525"},
    {   
        "Toll Gate Name": "Bankapur",
        "national_highway_id":"4",
        "Charges": "Return",
        "Car/Jeep/Van": "110",
        "LCV": "190",
        "2 Axle Bus, Truck": "300",
        "3 Axle Bus, Truck": "610",
        "4,5,6 Axle Bus, Truck": "610",
        "7 Axle Bus, Truck": "610",
        "Heavy Vehicle": "610"},
    {
        "Toll Gate Name": "Brahamarakotlu",
        "national_highway_id":"73",
        "Charges": "Return",
        "Car/Jeep/Van": "40",
        "LCV": "60",
        "2 Axle Bus, Truck": "125",
        "3 Axle Bus, Truck": "140",
        "4,5,6 Axle Bus, Truck": "200",
        "7 Axle Bus, Truck": "245",
        "Heavy Vehicle": "200"},
    {   
        "Toll Gate Name": "Chalageri",
        "national_highway_id":"4",
        "Charges": "Return",
        "Car/Jeep/Van": "115",
        "LCV": "185",
        "2 Axle Bus, Truck": "390",
        "3 Axle Bus, Truck": "425",
        "4,5,6 Axle Bus, Truck": "610",
        "7 Axle Bus, Truck": "740",
        "Heavy Vehicle": "810"},
    {   
        "Toll Gate Name": "Doddakarenahalli (Neelmangala)",
        "national_highway_id":"75",
        "Charges": "Return",
        "Car/Jeep/Van": "65",
        "LCV": "110",
        "2 Axle Bus, Truck": "220",
        "3 Axle Bus, Truck": "355",
        "4,5,6 Axle Bus, Truck": "355",
        "7 Axle Bus, Truck": "355",
        "Heavy Vehicle": "355"},
    {   
        "Toll Gate Name": "Gaddurur",
        "national_highway_id":"75",
        "Charges": "Return",
        "Car/Jeep/Van": "40",
        "LCV": "60",
        "2 Axle Bus, Truck": "130",
        "3 Axle Bus, Truck": "140",
        "4,5,6 Axle Bus, Truck": "205",
        "7 Axle Bus, Truck": "250",
        "Heavy Vehicle": "205"},
    {   
        "Toll Gate Name": "Gundmi",
        "national_highway_id":"66",
        "Charges": "Return",
        "Car/Jeep/Van": "65",
        "LCV": "105",
        "2 Axle Bus, Truck": "220",
        "3 Axle Bus, Truck": "345",
        "4,5,6 Axle Bus, Truck": "345",
        "7 Axle Bus, Truck": "420",
        "Heavy Vehicle": "345"},
    {   
        "Toll Gate Name": "Hattargi",
        "national_highway_id":"4",
        "Charges": "Return",
        "Car/Jeep/Van": "40",
        "LCV": "65",
        "2 Axle Bus, Truck": "140",
        "3 Axle Bus, Truck": "150",
        "4,5,6 Axle Bus, Truck": "220",
        "7 Axle Bus, Truck": "265",
        "Heavy Vehicle": "220"},
    {   
        "Toll Gate Name": "Surathkal",
        "national_highway_id":"66",
        "Charges": "Return",
        "Car/Jeep/Van": "80",
        "LCV": "125",
        "2 Axle Bus, Truck": "265",
        "3 Axle Bus, Truck": "290",
        "4,5,6 Axle Bus, Truck": "415",
        "7 Axle Bus, Truck": "505",
        "Heavy Vehicle": "415"},
    {   
        "Toll Gate Name": "Talapady",
        "national_highway_id":"66",
        "Charges": "Return",
        "Car/Jeep/Van": "60",
        "LCV": "90",
        "2 Axle Bus, Truck": "185",
        "3 Axle Bus, Truck": "280",
        "4,5,6 Axle Bus, Truck": "280",
        "7 Axle Bus, Truck": "360",
        "Heavy Vehicle": "280"}	
        ]

@app.route('/')
def index():
    return "Welcome to the TOLL GATE CHARGES OF KARNATAKA API:" 

@app.route("/tolls",methods=['GET'])
def get():
    return jsonify(
    {'TOLL GATE CHARGES ON A TWO WAY BASIS': tollsr},
    {'TOLLS GATE CHARGES ON A SINGLE WAY BASIS': tollsd},
    {'TOLL GATE CHARGES ON A MONTHLY BASIS': tollsm})






@app.route("/tolls/<int:national_highway_id>",methods=['GET'])
def get_Specific_Highway_charges_twoway(national_highway_id):
    return jsonify(
    {'TOLL GATE CHARGES ON A TWO WAY BASIS': tollsr[national_highway_id]},
    {'TOLLS GATE CHARGES ON A SINGLE WAY BASIS': tollsd[national_highway_id]},
    {'TOLL GATE CHARGES ON A MONTHLY BASIS': tollsm[national_highway_id]})


if __name__ == "__main__":
    app.run(debug=True,port='8085')


