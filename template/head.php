<h1>
    Welcome on this website!
</h1>
<nav class="menu">
    <div>
        <?php
            $nav_items = config('nav_menu');
            $namelist = '';
            foreach ($nav_items as $uri => $name) {
                $namelist .= '<a href="">'.$name.'</a>'.'<a class="dropdown">dropdown</a>';
            }
            echo $namelist;
        ?>
    </div>
</nav>