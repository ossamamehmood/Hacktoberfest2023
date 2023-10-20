function talk(){
        
    var know = {
        //on met les phrases qui seront utiliser pour chercher les reponses
        //et on place après : les reponses des phrases 
        "who are you": "hello, luminos_code here ",
        "how are you":"i'm good ",
        "what can i do for you": "search lmr_code on google >>>thank me later",
        "your follower" : "i have my familly of 609 members,i don't have follower ,have supportive familly",
        "ok":"thank you so much",
        bye:"okay! will meet soon ...",
        "moi":"lmr",
        "comment tu vas":"je vais bien et vous?",
        "ton nom":"je m'appelle chatbot !!",
        "tu as quel age":"je suis une intelligence artificiel est je ne peut pas avoir d'age ,mais je peux te dire que j'ai été coder le 17 janvier 2023",
        "tu aimes quoi":"j'aimes la programmation,les humains,les casses tête .... et beaucoup d'autre chose plus geniale les unes que les autres !!!",
        "what is your language" :"my language is french and english ,but i learning the spainish " ,
        "who create you":"my creator is lmr LUMIERE",
        "what is your name":"my name is chartbot",
        "charbot":"yes ,is my name ",
        "why":"because,i'm combinaison between character and robot",
        "capital of drc":"The DRC capital is Kinshasa",
        "capital of french":"The French capital is Paris",
        "date your creation":"January,10th 2023",
        "what is time":"see in navbar",
        "give me time":"see in navbar ",
        "give me second":"secondd is ",
        "help me":"i don't help you,but you aren't connect to internet",
        "what":"what is relative pronoun in english",
        "who":"who is the personnal pronoun in english",
        "when":"when is the relative pronoun in english",
        "who is the drc president":"the DRC president is Mr TsHISEKEDI THILOMBO Antoine",
        "who is the gouvenor of haut-katanga":"the gouvernor of Haut-Katanga is mr KIABULA KATWE Jack",
        "what you remember":"i remember much things",
        "you are congolese":"i dont have a nationality",
        "what is the superficy in congo":"the superficy in congo is 2345000",
        "bonsoir":"bonsoir à toi ",
        "tu fais quoi":"je suis assis et toi???",
        "moi aussi":"content de le savoir",


    };
    //on récupère la valeur saisi dans l'input
    var user=document.getElementById("userbox").value;
    //on la place sur id chatlog
    document.getElementById("chatlog").innerHTML = user + "<br>";
    if (user in know) {
        //on verifie si la phrase saisi existe dans la variable know
        //si la phrase existe on affiche sa réponse 
        document.getElementById("chatlog").innerHTML =know[user] + "<br>";
        
    } else {
        //si la phrase n'existe pas on envoie le message sorry...
            document.getElementById("chatlog").innerHTML ="sorry,i don't understand <br>";
        }
        
}
