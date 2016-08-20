$(function () {
  function check_messages() {
    $.ajax({
      url: '/messages/check/',
      cache: false,
      success: function (data) {
        $("#unread-count").text(data);
      },
      complete: function () {
        window.setTimeout(check_messages, 60);
      }
    });
  };
  check_messages();
});
