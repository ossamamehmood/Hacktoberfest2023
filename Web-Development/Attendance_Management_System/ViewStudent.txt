
<!DOCTYPE html>

<html lang = "en">

    <meta name = "viewport" content = "width = device-width, initial-scale = 1.0">
    <meta charset = "UTF-8">

    <title>
        Details Table 
    </title>

    <body background = "https://bit.ly/31A7CmL">

        <br> 

        <br> 

        <br>

        <p align = "center"> 

            <b>

                <font color = "#004d1a" face = "Lato">  

                    <h style = "font-size: 500%">    
                        Student Records
                    </h>

                </font>

            </b>    

        </p>

        <p align = "centre">

            <i>

                <font color = "#009933" face = "Comic Sans MS">

                    <h1 style = "font-size: 135%"> 
                        Add the basic information like Name, Roll Number, 
                        and Email ID of other students to view it in the following data table.
                   </h1> 

                </font>

            </i>

        </p>

        <?php

            error_reporting(0);
            include "DataBase.php";

            $sql = "SELECT * FROM `student` WHERE 1";
            $result = mysqli_query($connect, $sql);

            echo "<table border = '6', cellspacing = '2', cellpadding = '2', width = '1250', frame = 'box'> 

                <tr> 

                    <th> 

                        <i> 
                            Enrollment Number 
                        </i> 

                    </th> 

                    <th> 

                        <i> 
                            Full Name  
                        </i> 

                    </th> 

                    <th> 

                        <i> 
                            Official Email ID 
                        </i> 

                    </th> 

                </tr>";
            
                foreach($result as $row)

                {

                    echo 

                    "<tr> 

                        <td align = 'middle'> 

                            <b>"
                                .$row["roll"].
                            "</b> 

                        </td>

                        <td align = 'middle'> 

                            <b>"
                                .$row["name"].
                            "</b> 

                        </td>

                        <td align = 'middle'> 

                            <b>"
                                .$row["email"].
                            "</b> 

                        </td>

                    </tr>";

                }
                
            echo "</table>";

        ?>

        <br>

        <b>

            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

            <a href = "http://localhost/Project/HomePage.php"> 
                Home Page
            </a> 

        </b>

    </body>

</html>
