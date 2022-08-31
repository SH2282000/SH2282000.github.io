<?php
/**
 * Displays page content.
 * If not found, display 404 error page.
 */
function page_content($path)
{
    if (file_exists($path)) {
        include($path);
    } else echo file_get_contents('content/404.html');
}

?>