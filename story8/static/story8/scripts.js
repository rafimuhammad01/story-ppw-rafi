$(function() {
    $("#searchbox").keyup(function() {
        var element = $("#searchbox").val()

        $.ajax ({
            url: "/story8/data?q=" + element,
            success: function(e) {
                $('.search').css('margin-bottom', "10%")
                $('#content').empty();
                $('#content').append(`
                    <div class="row justify-content-center">
                        <div class='col col-md-12' style="padding-left:10%">
                            <h3>Search result :</h3>
                        </div>
                    </div>

                    <div id=content1 class="border border-light">

                    </div>    
                `)
                
                if(e.items != undefined) {
                    for (i = 0; i < e.items.length; i++) {
                        var title = e.items[i].volumeInfo.title;
                        var gambar = e.items[i].volumeInfo.imageLinks.smallThumbnail;
                        var publisher = e.items[i].volumeInfo.publisher;
                        var info = e.items[i].volumeInfo.infoLink;
                        var searchinfo = e.items[i].searchInfo.textSnippet;
                        $('#content1').append(`
                        
                            <div class='row' style=" text-align: left;">
                                <div class='col-sm-1 col-md-2  '>
                                    <img src='` + gambar + `'>
                                </div> 
                                <div class=' col-sm-1 col-md-10  '>
                                    <a href=`+info +` style="text-align: left;font-size: x-large; padding-bottom: 0; padding-top:3%">` + title + `</a>
                                    <p> publisher : ` + publisher + `</p>
                                    <p>  ` + searchinfo + `</p>
                                </div> 
                                
                                
                                        
                            </div>
                            <hr> 
                        `)
                    }
                
                } else {
                    $('#content1').append(`
                        
                            <div class='row' style=" text-align: left;">
                                <div class=' col-sm-1 col-md-10  '>
                                    <h1 style="text-align: left;font-size: x-large; padding-bottom: 0; padding-top:3%">` + 'not found.' + `</h1>
                                    
                                </div> 
                                
                                
                                        
                            </div>
                        `)
                }
                
                
            }
        })
    })
})