$(document).ready(function () {
  // Fetch translation from the URL
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    // Extract the translation of "hello" from the response
    const helloTranslation = data.hello;
    // Display the translation in the div with ID "hello"
    $('#hello').text(helloTranslation);
  })
    .fail(function (error) {
      // Handle errors
      console.error(error);
    });
});
