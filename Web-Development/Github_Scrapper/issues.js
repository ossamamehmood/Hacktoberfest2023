const request = require("request"); //module for request the data from server
const cheerio = require("cheerio"); //process and extract the html data
const fs=require('fs');
const path=require('path');
const pdfkit=require('pdfkit');

function getIssuesPageHTML(url, topic, repoName) {
  request(url, cb);
  function cb(err, response, html) {
    if (err) {
      console.log(err);
    } else if(response.statusCode==404){
        console.log("page not found, from issues");
    } 
    else {
      getIssues(html);
    //   console.log(html);
    }
  }

  function getIssues(html) {
    let $ = cheerio.load(html);
    let issueArr=$('.Link--primary.v-align-middle.no-underline.h4.js-navigation-open.markdown-title');
    let arr=[];
    console.log(issueArr.length);
    for (let i = 0; i < issueArr.length; i++) {
        let link=$(issueArr[i]).attr('href');
        // console.log(link);
        arr.push(link);        
    }

    // console.log(topic,":  ",arr);
    let folderpath=path.join(__dirname,topic);
    dirCreater(folderpath);
    let filepath=path.join(folderpath,repoName+".pdf");
    fs.writeFileSync(filepath,JSON.stringify(arr));  
    let text=JSON.stringify(arr);
    let pdfDoc=new pdfkit();
    pdfDoc.pipe(fs.createWriteStream(filepath));
    pdfDoc.text(text);
    pdfDoc.end(); 
  }
}

module.exports = getIssuesPageHTML;
function dirCreater(folderpath){
  if(fs.existsSync(folderpath)==false){
    fs.mkdirSync(folderpath);
  }
}