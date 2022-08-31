<header>
    <h1><?php site_name(); ?></h1>
    <nav class="menu">
        <?php nav_menu(); ?>
    </nav>
</header>

<article>
    <h2><?php page_title(); ?></h2>
    <?php page_content(); ?>
</article>

<footer>
    <small>&copy;<?php echo date('Y'); ?> <?php site_name(); ?>.<br><?php site_version(); ?></small>
</footer>