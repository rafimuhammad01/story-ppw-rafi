$( function() {
    $( "#accordion" )
      .accordion({
        header: "> div > h3 ",
        heightStyle: "content",
        collapsible: true ,
        clearStyle: true, 
        autoHeight: false,
        active: false,
        
      })
      
    $('.down').click(function(e){
      e.stopPropagation();
      var id = $(this).closest('.group').attr('id')

      if (id != 4) {
        var idNext = parseInt(id)+1

        $("#" + id).insertAfter($("#" + idNext))
        $("#" + id).attr('id', idNext)
        $("#" + idNext).attr('id', id)
      } 
      
    });

    $('.up').click(function(e){
      e.stopPropagation();
      var id = $(this).closest('.group').attr('id')

      if (id != 1) {
        var idPrev = parseInt(id)-1

        $('#' + id).insertBefore("#" + idPrev)
        $("#" + id).attr('id', 5)
        $("#" + idPrev).attr('id', id)
        $("#5").attr('id', idPrev)

        console.log($("#accordion").html())
        console.log(id)
        console.log(idPrev)
      }
    });

  } );