/* ------------------------------------------------------------------------------------
 *  COPYRIGHT AND TRADEMARK NOTICE
 *  Copyright 2001-2020 Abdulrahman Obaje. All Rights Reserved.
 *  obajesoft.com.ng is a trademark of ObajeSoft Inc.
 
 *  COPYRIGHT NOTICES AND ALL THE COMMENTS SHOULD REMAIN INTACT.
 *  By using this code you agree to indemnify Abdulrahman Obaje from any
 *  liability that might arise from it's use.
 ------------------------------------------------------------------------------------ */


function getTopics(id) {
    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("quizTopic").innerHTML = this.responseText;
        }
    };
    //alert(xhttp);
    //xhttp.open("GET", "<?php echo WEB_ROOT; ?>admin/quiz?task=getTopics", true);
    xhttp.open("GET", "<?php echo WEB_ROOT; ?>admin/quiz?task=getTopics&id=" + id, true);
    xhttp.send();
}