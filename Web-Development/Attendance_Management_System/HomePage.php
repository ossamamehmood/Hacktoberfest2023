
<!DOCTYPE html>

<html lang = "en">

    <meta name = "viewport" content = "width = device-width, initial-scale = 1.0">
    <meta charset = "UTF-8">
     
    <title>
        Menu Page
    </title>

    <script>
     window.location.hash = "no-back-button";
     window.location.hash = "Again-No-back-button";
     window.onhashchange = function() {window.location.hash="no-back-button";}
    </script> 

    <body background = "https://bit.ly/31A7CmL">

        <br>

        <br>

        <br>

        <p align = "center"> 

            <b>

                <font color = "#4d2600" face = "Lato">  

                    <h style = "font-size: 502%">    
                        Welcome CWIT
                    </h>

                </font>

            </b>    

        </p>

        <p align = "centre">

            <i>

                <font color = "#994d00" face = "Comic Sans MS">

                    <h1 style = "font-size: 133%"> 
                        From the different options provided in the space below, 
                        choose the one you wish to use this application for and proceed ahead.
                    </h1> 

                </font>

            </i>

        </p>

    </body>

    <div class = "menu">

        <?php 

            error_reporting(0);
            include "BaseMenu.php";

        ?>

    </div>

</html>
