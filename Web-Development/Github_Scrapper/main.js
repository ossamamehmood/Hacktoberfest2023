let url='https://github.com/topics';
const request=require('request');  //module for request the data from server
const cheerio=require('cheerio');   //process and extract the html data
let getreposPage=require('./getRepos');
// console.log('before');
request(url,callback);   
//html data
function callback(error,response,html){
    if(error){
        console.log('there is an error');
    } else if(response.statusCode==404){
        console.log("page not found :from main");
    } 
    else{
        // console.log(html);     //can store this data in a file using os module
        getTopicLinks(html);
    }
}

function getTopicLinks(html){
    let $=cheerio.load(html); //getting element containing links of elements
    let linkElemArr=$(".no-underline.d-flex.flex-column.flex-justify-center");
    for(let i=0;i<linkElemArr.length;i++){
        let href=$(linkElemArr[i]).attr("href");   //getting elements href
        let topic=href.split("/").pop();
        let fulllink=`https://github.com/${href}`;
        // console.log(fulllink);
        getreposPage(fulllink,topic);
        // console.log(href);
    }
}