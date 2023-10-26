
<!DOCTYPE html>

<html>

  <?php

    echo "<b>";

      error_reporting(0);

      $servername = "localhost";
      $username = "root";
      $password = "";
      $database = "attendance";

      $connect = mysqli_connect($servername, $username, $password, $database);

      if (!$connect)

        {

          die ("___________________________________Failed to establish a connection: ".mysqli_connect_error().
          ".___________________________________");

        }

      else

        {

          echo "________________________________________________The details will be recorded 
          as a connection to the database has been established.________________________________________________<br> <br>";

        }

      echo "</b>";

  ?>

</html>
