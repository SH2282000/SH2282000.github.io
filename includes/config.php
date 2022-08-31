<?php

/**
 *  website configuration information.
 * 
 * @var string or null
 */
function config($key = '')
{
    $config = [
        'name' => 'ShannahBANANA',
        'site_url' => 'bananananana.com',
        'pretty_uri' => false,
        'nav_menu' => [
            '' => 'Home',
            'cv' => 'What I Did',
            'projects' => 'What I Like',
            'contact' => 'Contact',
        ],
        'version' => 'v0.1',
    ];

    return isset($config[$key]) ? $config[$key] : null;
}