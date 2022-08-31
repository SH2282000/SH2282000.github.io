<!DOCTYPE html>
<html>
    <?php
        require 'includes/config.php';
        require 'includes/functions.php';
    ?>
    <?php page_content('template/header.html') ?>
    <body>
        <?php page_content('template/head.php') ?>
        <div class="blueBanner">
            <img src="src/img/profile_shannah1.png">
            <div class="content">
                <h1>
                    Hello, I'm Shannah
                </h1>
                <h2>We're on the same boat.</h2>
                <p>
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime, doloremque quaerat ducimus qui provident harum ratione laboriosam hic quo omnis nam at, consequatur illo? Id debitis ducimus nisi suscipit dolore!
                </p>
            </div>
        </div>
        <?php page_content('template/footer.html') ?>
    </body>
</html>