import tkinter
import tkinter.messagebox
import random
screen = tkinter.Tk()
screen.geometry("400x400")
screen.title("jumbled word game")
#words=[] 
jumbledword = "ym mena si terbor"
titlee = tkinter.Label(screen , text=  "JUMBLED WORD GAME" , font = ("arial" , 25) )


jw = ["apple","banana","cherry","dragon","island","palace","statue","temple","desert","jungle","canyon","meadow","orchard","timber","breeze","thunder","summit","crater","galaxy","cosmos",
      "nebula","meteor","vector","signal","matrix","cipher","symbol","knight","shield","sword","legend","journey","treasure","wisdom","nature","harbor","market","bridge","garden","valley",
      "castle","stream","planet","silver","bright","fresh","clean","strong","swift","happy","brave","smile","laugh","dream","winner","listen","dance","school","teacher","student","parent",
      "family","friend","peace","world","village","window","table","chair","screen","glass","letter","number","phone","paper","shadow","music","flower","forest","stone","cloud","mountain",
      "ocean","house","river","camera","laptop","server","memory","module","thread","buffer","stream","socket","kernel","domain","script","plugin","canvas","widget","toggle","button",
      "slider","prompt","vector","raster","format","import","export","output","result","render","engine","action","method","target","member","symbol","syntax","string","number","double",
      "object","array","struct","schema","native","global","public","static","inline","extern","return","lambda","filter","reduce","mapset","caller","handle","router","client","border",
      "margin","column","offset","height","weight","header","footer","navbar","layout","drawer","modal","dialog","notice","banner","canvas","shadow","border","radius","stroke","fillin",
      "accent","contrast","vector","aspect","ration","aspect","volume","length","charge","energy","power","joule","kelvin","pascal","hertz","ampere","curie","sievert","dalton","newton",
      "degree","radian","second","minute","hourly","daily","weekly","monthly","yearly","spring","summer","autumn","winter","season","period","epoch","decade","century","millis","second",
      "minute","future","pasttime","present","ancient","modern","future","cosmic","global","native","locale","region","county","nation","empire","colony","border","domain","region",
      "street","avenue","tunnel","bridge","pathway","avenue","highway","harbor","airport","subway","transit","engine","motor","piston","valves","torque","clutch","brakes","wheels",
      "timing","exhaust","inlet","filter","gasket","spark","charge","cooler","heater","sensor","wiring","cable","switch","relay","socket","module","sensor","driver","device","system",
      "memory","diskette","volume","sector","format","backup","restore","repair","update","upgrade","reboot","unload","upload","download","commit","branch","merged","rebase","revert",
      "stashing","cherry","origin","remote","target","master","worker","daemon","process","thread","tasker","runner","jobset","queue","stream","socket","pipein","output","logger",
      "tracer","metric","metric","alerts","status","health","active","paused","closed","failed","finish","latest","stable","canary","legacy","custom","native","default","sample",
      "template","option","select","choice","picked","action","events","target","source","parent","childs","sibling","ancestor","middle","center","topmost","bottom","inside","outside",
      "border","margin","padded","spaced","shadow","opaque","blurry","bright","darken","color","reddish","blueish","greeny","yellow","purple","orange","silver","golden","bronze","copper"
      ,"nickel","cobalt","chrome","carbon","silicon","oxygen","carbon","sulfur","sodium","radium","uranium","lithium","helium","xenon","krypton","argon","neon","radon","lead","iron","tin"
      ,"zinc","copper","brass","bronze","timber","marble","granite","basalt","quartz","flint","cement","mortar","bricks","plaster","asphalt","glassy","fabric","cotton","woolen","velvet"
      ,"linen","satin","leather","canvas","rubber","plastic","nylon","kevlar","teflon","carbon","poly","resin","latex","sponge","foam","felt","timber","bamboo","willow","spruce","redwood"
      ,"sequoia","cypress","juniper","magnolia","jasmine","orchid","violet","daisy","tulip","lilac","peony","dahlia","azalea","cactus","bamboo","bonsai","clover","thistle","hemlock",
      "walnut","almond","cashew","peanut","hazel","pecan","pistachio","sesame","grape","raisin","fig","date","prune","lemon","lime","orange","papaya","guava","mango","banana","melon",
      "berry","cherry","peach","plum","apricot","nectar","lychee","durian","pomelo","quince","medlar","elderly","mulberry","soursop","tangerine","mandarin","coconut","citrus","citron"
      ,"feijoa","kumquat","loquat","rambutan","jackfruit","persimmon","plantain","avocado","spinach","cabbage","lettuce","kale","celery","garlic","onion","shallot","scallion","radish"
      ,"turnip","carrot","beetroot","parsnip","cassava","yam","potato","tomato","pepper","chili","ginger","turmeric","mustard","nutmeg","cinnamon","vanilla","saffron","paprika","oregano"
      ,"rosemary","coriander","parsley","cilantro","basil","thyme","sage","mint","tarragon","cardamom","fennel","clove","allspice","caraway","wasabi","horseradish","matcha","lavender",
      "chamomile","hibiscus","chicory","espresso","cappuccino","macchiato","cortado","american","latte","mocha","ristretto","smoothie","cocktail","mocktail","lemonade","smoothie","cider",
      "sherry","brandy","whiskey","bourbon","liqueur","absinthe","vermouth","tequila","mezcal","aquavit","seltzer","tonic","nectar","cordial","tisane","compote","pudding","custard","gelato",
      "sherbet","sorbet","mousse","parfait","cobbler","crumble","brownie","cupcake","muffin","pancake","waffle","croissant","brioche","baguette","pretzel","biscuit","cookie","pastry","strudel",
      "baklava","cannoli","macaron","tartlet","shortcake","fruitcake","eclair","tiramisu","souffle","fondue","praline","truffle","caramel","fudge","toffee","marshmallow","licorice","gumdrop",
      "lollipop","bonbon","nougat","marzipan","meringue","compote","gelatin","pectin","glucose","fructose","sucrose","lactose","maltose","starch","protein","peptides","enzyme","hormone","vitamin",
      "mineral","calcium","sodium","potassium","magnesium","chloride","sulfate","nitrate","ammonia","methane","propane","butane","ethanol","acetone","benzene","toluene","styrene","polymer",
      "monomer","solvent","catalyst","reagent","isotope","nucleus","electron","proton","neutron","photon","quark","boson","lepton","hadron","gluon","meson","neutrino","graviton","tachyon",
      "fermion","baryon","positron","muon","pion","kaon","hyperon","monopole","quantum","atomics","molecule","lattice","crystal","amorphous","polymer","colloid","aerosol","emulsion","solute",
      "solvent","mixture","element","compound","isotope","isomer","monomer","polymorph","catalyst","reagent","analyte","titrant","residue","distillate","extract","filtrate","precipitate",
      "slurry","eluate","effluent","solvent","hydrate","anhydrous","viscous","volatile","corrosive","caustic","toxic","flammable","reactive","inert","stable","unstable","radiant","thermal",
      "kinetic","elastic","gravitas","magnetic","electric","acoustic","optical","nuclear","dynamic","static","thermal","potential","radiant","friction","viscous","tension","torsion",
      "impulse","momentum","inertia","velocity","speed","vector","scalar","tensor","matrix","orbital","azimuth","zenith","ecliptic","apogee","perigee","aphelion","perihelion","parallax",
      "solstice","equinox","transit","eclipse","occultation","syzygy","cluster","nebula","pulsar","quasar","supernova","singularity","horizon","continuum","manifold","geodesic",
      "spaceband","cosmology","astronomy","astrophysics","telemetry","altitude","latitude","longitude","azimuth","bearing","compass","headway","crosswind","tailwind","airspeed",
      "altitude","payload","thruster","booster","fairing","capsule","shuttle","orbiter","lander","rover","probe","satellite","station","spaceport","pad","gantry","umbilical",
      "countdown","liftoff","apogee","reentry","splashdown","recovery","telemetry","avionics","guidance","thruster","attitude","scuttling","docking","berthing","airlock",
      "space","visor","tether","jetpack","habitat","outpost","colony","terraforming","biosphere","ecosystem","habitat","biome","tundra","taiga","savanna","pampa",
      "steppes","prairie","woodland","chaparral","wetland","mangrove","estuary","lagoon","reef","atoll","archipelago","peninsula","isthmus","strait","channel",
      "fjord","glacier","iceberg","shelf","geyser","caldera","volcano","plateau","mesa","butte","canyon","ravine","gorge","valley","basin","dune","oasis",
      "badlands","savanna","wetland","swamp","marsh","bogland","fenland","delta","estuary","lagoon","creek","stream","brook","branch","river","rapid",
      "waterfall","cascade","geyser","aquifer","reservoir","cistern","fountain","artesian","estuary","harbor","marina","dockyard","wharf","pier",
      "jetty","quay","haven","inlet","cove","bayou","gulf","strait","channel","sound","basin","reach","roadstead","anchorage" ]
now = 499
userwins= 0
def jumble():
    global now, jumbled , wordgenerated
    wordgenerated = jw[random.randint(0,now)]
    now = 499-1
    lettertbj = []
    for i in range(len(wordgenerated)):
        lettertbj.append(wordgenerated[i])
    jw.remove(wordgenerated)
    random.shuffle(lettertbj)
    jumbled = "".join(lettertbj)
    jumbledword.config(text = jumbled)

def answer():
    global wordgenerated , userwins
    user = useranswer.get()
    if wordgenerated == user:
        tkinter.messagebox.showinfo(title = "winner" , message="well done , you got the answer correct." )
        userwins = userwins+1
        userwinZ.config(text=f"you won {userwins} games")
        jumble()
        useranswer.delete(0 , tkinter.END)
    elif wordgenerated != user:
        tkinter.messagebox.showwarning(title="incorrect" , message = "incorrect try again ")


userwinZ = tkinter.Label(screen , text=f"you won {userwins} games", font =( "arial", 15))
jumbledword = tkinter.Label(screen , text = ""  , font = ("arial ", 15))
useranswer = tkinter.Entry(screen , font=("arial" , 20))
enter = tkinter.Button(screen , text = "Enter" , background="dark gray" , fg = "yellow" , font=("arial"  , 25) , command= answer)
next = tkinter.Button(screen, text = "Next" , background = "gray" , fg = "yellow" , font= ("arial ",25), command=jumble)
jumble()
titlee.pack(pady= 20)
userwinZ.pack(pady=10)
jumbledword.pack(pady = 10)
useranswer.pack(pady = 10)
enter.pack(pady = 10)
next.pack(pady = 10)



screen.mainloop()