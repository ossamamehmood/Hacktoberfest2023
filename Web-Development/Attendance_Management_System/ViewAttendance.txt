
<!DOCTYPE html>

<html lang = "en">

    <meta name = "viewport" content = "width = device-width, initial-scale = 1.0">
    <meta charset = "UTF-8">

    <title>
        Attendance Table 
    </title>

    <body background = "https://bit.ly/31A7CmL">

        <br> 

        <br> 

        <br>

        <p align = "center"> 

            <b>

                <font color = "#4d3900" face = "Lato">  

                    <h style = "font-size: 500%">    
                        Attendance Records
                    </h>

                </font>

            </b>    

        </p>

        <p align = "centre">

            <i>

                <font color = "#997000" face = "Comic Sans MS">

                    <h1 style = "font-size: 135%"> 
                        Mark the attendance of the students for any date based on their
                        enrollment numbers to view it in the following data table.
                    </h1> 

                </font>

            </i>

        </p>

        <?php

            include "DataBase.php";
            error_reporting(0);

            $sql = "SELECT * FROM `record` WHERE 1";
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
                            Date  
                        </i> 

                    </th> 

                    <th> 

                        <i> 
                            Attendance 
                        </i> 

                    </th> 

                </tr>";
            
                foreach ($result as $row)

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
                                .$row["date"].
                            "</b> 

                        </td>

                        <td align = 'middle'> 

                            <b>"
                                .$row["status"].
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
