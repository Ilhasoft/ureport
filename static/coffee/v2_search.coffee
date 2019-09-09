# wire in our search boxes
$(->
  $(".search-box").focusin(->
    results = $(this).data("results-id")
    $("#" + results).show().addClass("shown")
  )

  $(".search-box").on('blur', ->
    $(this).val("")
    results = $(this).data("results-id")
    $("#" + results).hide().removeClass("shown")
  )

  $(".search-box").keyup(->
    filter = $(this).val().toLowerCase()
    results = $(this).data("results-id")

    if filter == ""
      $("#" + results).find(".searchable").removeClass("hidden")

    $("#" + results).find(".searchable").each(->
      value = $(this).data("search-value")
      if value.toLowerCase().indexOf(filter) >= 0
        $(this).removeClass("hidden")
      else
        $(this).addClass("hidden")
    )
  )
)