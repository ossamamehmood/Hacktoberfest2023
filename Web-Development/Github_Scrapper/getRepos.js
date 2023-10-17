const request = require("request"); //module for request the data from server
const cheerio = require("cheerio"); //process and extract the html data
let getIssues=require("./issues");
function getreposPageHTML(url,topic) {
  request(url, cb);
  function cb(err, response, html) {
    if (err) {
      console.log();
    } else if(response.statusCode==404){
        console.log("page not found ,from getRepos");
    }  
    else {
    //   console.log(html);
      getReposLink(html);
    }
  }

  function getReposLink(html) {
    let $ = cheerio.load(html);
    let headingArr = $(".f3.color-fg-muted.text-normal.lh-condensed");
    console.log(topic);
    for (let index = 0; index < 8; index++) {
      let twoAnchors = $(headingArr[index]).find("a");     //getting repos 
      let link = $(twoAnchors[1]).attr("href");
      let fulllink=`https://github.com/${link}/issues`;
      let repoName=link.split("/").pop();
      getIssues(fulllink,topic,repoName);
    }
    console.log("`````````````````````````````````````````````````````````````");
  }
}

module.exports = getreposPageHTML;
