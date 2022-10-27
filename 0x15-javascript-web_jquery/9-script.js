$.get("https://fourtonfish.com/hellosalut/?lang=fr", (res) => {
    $("DIV#hello").text(res.hello);
})
