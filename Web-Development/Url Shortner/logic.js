let btn = document.getElementById("short");

btn.addEventListener('click',short);

async function short(){
    let longurl = document.getElementById("longurl").value;

    const result = await fetch(`https://api.shrtco.de/v2/shorten?url=${longurl}`);
   const data = await result.json();
   
   shorturl.value = data.result.short_link2;
   console.log(data.result.short_link2);
}