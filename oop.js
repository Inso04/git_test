//Oppg 1a
class Land {
    constructor(navn, areal, folketall){
    //setter ulike parameter
    this.navn = navn;
    this.areal = areal;
    this.folketall = folketall;
    }
    //Oppgave 1d
    get innbyggerePerKvadratmeter(){
        return this.folketall / (this.areal * 1000000);
    }
    LandInfo(){
        return(document.write(this.navn+ " er " +this.areal+ " kvadratkilometer, har " +this.folketall+ " innbyggere, og har " +this.innbyggerePerKvadratmeter+ " innbyggere per kvadratmeter."));
    }
}

//Oppgave 1b
var norge = new Land("Norge", 385207, 1);
var sverige = new Land("Sverige", 528447, 2);
var danmark = new Land("Danmark", 42951, 3);
var tyskland = new Land("Tyskland", 357588, 4);

//Oppgave 1c
norge.folketall = 5408000;
sverige.folketall = 10420000;
danmark.folketall = 5857000;
tyskland.folketall = 83200000;

norge.LandInfo()
sverige.LandInfo()
danmark.LandInfo()
tyskland.LandInfo()

//Siden jeg kan velge to av de fire oppgavene i oppg. 2 så velger jeg 2a og b
//Oppgave 2a
class TVserie {
    constructor(tittel, år, hovedrolle){
        this.tittel = tittel;
        this.år = år;
        this.hovedrolle = hovedrolle;
    }
    TVserieInfo() {
        return(document.write(this.tittel+ " begyte i " +this.år+ " og hovedkarakteren heter " +this.hovedrolle+ "."));
    }
}
var atla = new TVserie("Avatar: The Last Airbender", 2005, "Aang");
var alok = new TVserie("Avatar: Legend of Korra", 2012, "Korra");
var op = new TVserie("One Piece", 1999, "Monkey D. Luffy");
var aot = new TVserie("Attack on Titan", 2013, "Eren Yeager");

atla.TVserieInfo()
alok.TVserieInfo()
op.TVserieInfo()
aot.TVserieInfo()

//Oppgave 2b
class Matvare {
    constructor(navn, karbohydrater, proteiner, fett, salt){
        this.navn = navn;
        this.karbohydrater = karbohydrater;
        this.proteiner = proteiner;
        this.fett = fett;
        this. salt = salt;
    }
    MatvareInfo(){
        return(document.write(this.navn+ " har " + this.karbohydrater+ " gram karbohydrater, har " +this.proteiner+ " gram proteiner, har " +this.fett+ "gram fett, og har " +this.salt+ " gram salt."));
    }
}

var nugatti = new Matvare("Nugatti", 62, 4.6, 28, 0.18);
var smør = new Matvare("Bremykt", 0.5, 0.5, 82, 1);
var leverpostei = new Matvare("Leverpostei", 3.5, 9.9, 19, 1.5);
var ost = new Matvare("Norvegia", 0, 27, 27, 1.2);

nugatti.MatvareInfo()
smør.MatvareInfo()
leverpostei.MatvareInfo()
ost.MatvareInfo()

//Oppgave 3a
class Musikkinstrument {
    constructor(type, pris){
        this.type = type;
        this.pris = pris;
    }
}
class Strenginstrument extends Musikkinstrument {
    constructor(type, pris, antallStrenger){
        super(type, pris);
        this.antallStrenger = antallStrenger;
    }
}

//Oppgave 3b
var trompet = new Musikkinstrument("Blåseinstrument", 3000);
var fiolin = new Strenginstrument("Strenginstrument", 4000, 4);

document.write("Trompeten er et " +trompet.type+ " som koster " +trompet.pris+ " kr.");
document.write("Fiolinen er et " +fiolin.type+ " som koster " +fiolin.pris+ " kr, og har " +fiolin.antallStrenger+ " strenger.");