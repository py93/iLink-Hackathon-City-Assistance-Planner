function loadIframe(iframeName, url) {
    var $iframe = $('#' + iframeName);
    if ( $iframe.length ) {
        $iframe.attr('src',url);    // here you can change src
        return false;
    }
    return true;
}

function cancelsubmit(e)
{
    alert("Hello");
    e.preventDefault();
    someBug();
    return false;
}

// function hideNav()
// {
//     $("#curtain").fadeOut();
//     $("#direction").fadeOut();
// }

// function showNav()
// {
//     $("#curtain").fadeIn();
//     $("#direction").fadeIn();
// }


