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
      .sortable({
        axis: "y",
        handle: ".arrow",
        stop: function( event, ui ) {
          // IE doesn't register the blur when sorting
          // so trigger focusout handlers to remove .ui-state-focus
          ui.item.children( ".arrow" ).triggerHandler( "focusout" );
 
          // Refresh accordion to handle new order
          $( this ).accordion( "refresh" );
        }

      });
  } );