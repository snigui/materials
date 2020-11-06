var filters = [];
var finalData = {"filters": filters};
var f = 1;



$(document).ready(function(){
  let newFilt = {'filters': []};
  $.ajax({
    url : '/',
    type: 'POST',
    dataType: 'json',
    data: JSON.stringify(newFilt),
    contentType:"application/json; charset=UTF-8",
    success: function (data) {
      console.log(JSON.stringify(newFilt))
      //$("p").text(JSON.stringify(finalData));
      //alert(JSON.stringify(finalData));
    }
  })
  $.ajax({
    url : '/table',
    type: 'POST',
    dataType: 'json',
    data: JSON.stringify(newFilt),
    contentType:"application/json; charset=UTF-8",
    success: function (data) {
      console.log(JSON.stringify(newFilt))
      //$("p").text(JSON.stringify(finalData));
      //alert(JSON.stringify(finalData));
    }
  })
  setTimeout(function () {
  $('#dash-table').attr('src', $('#dash-table').attr('src'));
  }, 1600);
  var firstLoad = true;
  var cols= JSON.parse($("#filters").attr("name"));
  var selectCount = 1;
  console.log(cols);
  if (firstLoad){
    firstLoad = false;
    for(var i = 0; i < cols.length; i++) {
      $('#colNames1 select').append('<option value='+cols[i]+'>'+cols[i]+'</option>');
    }
  }
  var wrapperF = $(".filters");
  var filter_add = $(".addFilter");
  $(".filters").on('change', ".dropdown0", function(){
    console.log("from  funcccccccccccccccccc old f " + f);
    $(this).attr('class', 'dropdown' + f.toString());
    f++;
    var idee = "f" + f.toString();
    $(wrapperF).append('<div id="colNames' + f.toString() + '"><input type="filterText0" class="add_field" name="filter0" id="e' + f.toString() +'"><select class="dropdown0" id="d' + f.toString() + '"></select><input type="filterText" class="add_field" name="filter" id=' + idee + '><a href="#" id=' + idee + ' class="remove_field">Remove</a></div>');
    var newSelector = "colNames" + f.toString() + " select"
    for(var i = 0; i < cols.length; i++) {
       $('#'+newSelector).append('<option value='+cols[i]+'>'+cols[i]+'</option>');
    }
  });
  // $("select[class=dropdown0]").on('change',function(){
  //   console.log("from  funcccccccccccccccccc " + $(this).className)
  //   var ided = "d" + f.toString();
  //   var iremove = "f" + f.toString();
  //   $(this).attr('class', 'dropdown' + selectCount.toString());
  //   $('#colNames' + f.toString()).append('<a href="#" id=' + iremove + ' class="remove_field">Remove</a>');
  //   console.log("which dropdown" + selectCount);
  //   selectCount++;
  //   f++;
  //   var idee = "f" + f.toString();
  //   $(wrapperF).append('<div id="colNames' + f.toString() + '"><input type="filterText0" class="add_field" name="filter0" id="e' + f.toString() +'"><select class="dropdown0" id="d' + f.toString() + '"></select><input type="filterText" class="add_field" name="filter" id=' + idee + '></div>');
  //   var newSelector = "colNames" + f.toString() + " select"
  //   for(var i = 0; i < cols.length; i++) {
  //      $('#'+newSelector).append('<option value='+cols[i]+'>'+cols[i]+'</option>');
  //   }
  // });
  // $(".filters").click(function(){
  //   $('select[class="dropdown0"]').on('change', function(){
  //   console.log("gmmmmmmmmmmmmmmmmmmmmmmmm" + $(this).html());
  //   var ided = "d" + f.toString();
  //   var iremove = "f" + f.toString();
  //   $(this).attr('class', 'dropdown' + selectCount.toString());
  //   $('#colNames' + f.toString()).append('<a href="#" id=' + iremove + ' class="remove_field">Remove</a>');
  //   console.log("which dropdown" + selectCount);
  //   selectCount++;
  //   f++;
  //   var idee = "f" + f.toString();
  //   $(wrapperF).append('<div id="colNames' + f.toString() + '"><input type="filterText0" class="add_field" name="filter0" id="e' + f.toString() +'"><select class="dropdown0" id="d' + f.toString() + '"></select><input type="filterText" class="add_field" name="filter" id=' + idee + '></div>');
  //   var newSelector = "colNames" + f.toString() + " select"
  //   for(var i = 0; i < cols.length; i++) {
  //      $('#'+newSelector).append('<option value='+cols[i]+'>'+cols[i]+'</option>');
  //   }
  // });
// });

//have call back function in js for when a change is done in
//filters div and in the callback, loop through each div and check if dropdown0 has a value that isnt choose filter
//if so, then append a new dropdown, and make it's name dropdown 0, the other dropdown names dont really matter
//this is the new drop down


// if ($(this).val() != "choose filter"){
//   console.log("chaneddddddd")
//   //<a href="#" id=' + idee + ' class="remove_field">Remove</a>
//   selectCount++;
//   console.log("dropdown stuff");
//   f++;
//   var idee = "f" + f.toString();
//   $(wrapperF).append('<div id="colNames' + f.toString() + '"><input type="filterText0" class="add_field" name="filter0" id="e' + f.toString() +'"><select name="dropdown" id="d' + f.toString() + '"></select><input type="filterText" class="add_field" name="filter" id=' + idee + '></div>');
//   var newSelector = "colNames" + f.toString() + " select"
//   for(var i = 0; i < cols.length; i++) {
//      $('#'+newSelector).append('<option value='+cols[i]+'>'+cols[i]+'</option>');
//   }
//   for(var i = 1; i < f-1; i++) {
//     var oldSelector = "colNames" + i.toString()
//     console.log("old ones that need remove" + oldSelector)
//     var ide = "f" + i.toString();
//      $('#'+oldSelector).append('<a href="#" id=' + ide + ' class="remove_field">Remove</a>');
//   }
// }
    // console.log("dropdown stuff");
    // f++;
    // var idee = "f" + f.toString();
    // console.log("~~~~~???????????????~~~~~~~~~~~~~")
    // console.log(cols)
    // $(wrapperF).append('<div id="colNames' + f.toString() + '"><input type="filterText0" class="add_field" name="filter0" id="e' + f.toString() +'"><select class="clicked" id="d' + f.toString() + '"></select><input type="filterText" class="add_field" name="filter" id=' + idee + '><a href="#" id=' + idee + ' class="remove_field">Remove</a></div>');
    // var newSelector = "colNames" + f.toString() + " select"
    // for(var i = 0; i < cols.length; i++) {
    //    $('#'+newSelector).append('<option value='+cols[i]+'>'+cols[i]+'</option>');
    // }
  // $(filter_add).click(function(e){
  //   //console.log("add desc clicked!");
  //   e.preventDefault();
  //   f++;
  //   var idee = "f" + f.toString();
  //   console.log("~~~~~???????????????~~~~~~~~~~~~~")
  //   console.log(cols)
  //   $(wrapperF).append('<div class="dropdown" id="colNames' + f.toString() + '"><input type="filterText0" class="add_field" name="filter0" id="e' + f.toString() +'"><select id="d' + f.toString() + '"></select><input type="filterText" class="add_field" name="filter" id=' + idee + '><a href="#" id=' + idee + ' class="remove_field">Remove</a></div>');
  //   var newSelector = "colNames" + f.toString() + " select"
  //   for(var i = 0; i < cols.length; i++) {
  //      $('#'+newSelector).append('<option value='+cols[i]+'>'+cols[i]+'</option>');
  //   }
  //   // var idee1 = "e" + (f - 1).toString();
  //   // var idee2 = "f" + (f - 1).toString();
  //   // var idee3 = "d" + (f - 1).toString();
  //   // //join the item as a big string to append to filters with colname, lower, upper
  //   // var lower = $("#"+idee1).val();
  //   // var upper = $("#"+idee2).val();
  //   // var colFilter = $("#"+idee3).val();
  //   // var finalFilterString =  colFilter + "," + lower + "," + upper;
  //   // filters.push(finalFilterString);
  //   // console.log("++++++++++++");
  //   // console.log(filters);
  //   // console.log("++++++++++++");
  //   //console.log(data);
  // });

  $(wrapperF).on("click", ".remove_field", function(e){
    if (f == 2){
      console.log("last one!!!!!!!!");
      $('#colNames1').find("select").attr('class', 'dropdown0');
    }
    //console.log(this.id);
    var onlyNum = this.id.toString().slice(-1);
    var index = onlyNum -1;
    //console.log("~~~~~~~~~~~~~~~~~~~~`` remove of desc");
    //console.log(index);
    filters.splice(index, 1);
    //console.log("old pdcount");
    //console.log(d);
    f--;
    //console.log("new d count");
    //console.log(d);
    //console.log("the index");
    //console.log(d);
    e.preventDefault(); $(this).parent('div').remove();
    $(".remove_field").each(function(){
      if (this.id > index+1){
        this.id = this.id -1;
      }
    });
    $(".add_field").each(function(){
      if (this.id > index+1){
        this.id = this.id -1;
      }
    });
    console.log("After remove");
    console.log(filters);
  });
  // $("#fs").load(function(){
  //   $('#submittedFilters').text(filtersEntered);
  // });

  $('form').on('submit', function(event){
    filters = []
    console.log("value of f issssssss" + f)
    for(var i = 0; i < f+1; i++) {
      var idee1 = "e" + (i).toString();
      var idee2 = "f" + (i).toString();
      var idee3 = "d" + (i).toString();
      //join the item as a big string to append to filters with colname, lower, upper
      var lower = $("#"+idee1).val();
      var upper = $("#"+idee2).val();
      var colFilter = $("#"+idee3).val();
      if (colFilter != "choose"){
        var finalFilterString =  colFilter + "," + lower + "," + upper;
        filters.push(finalFilterString);
      }
      console.log("++++++++++++");
      console.log(filters);
      console.log("++++++++++++");
    }

    $(this).target = "_blank";
    $.ajax({
      url : '/',
      type: 'POST',
      dataType: 'json',
      data: JSON.stringify({"filters": filters}),
      contentType:"application/json; charset=UTF-8",
      success: function (data) {
        console.log(JSON.stringify({"filters": filters}))
        //$("p").text(JSON.stringify(finalData));
        //alert(JSON.stringify(finalData));
      }
    })
    $.ajax({
      url : '/table',
      type: 'POST',
      dataType: 'json',
      data: JSON.stringify(),
      contentType:"application/json; charset=UTF-8",
      success: function (data) {
        console.log(JSON.stringify(finalData))
        //$("p").text(JSON.stringify(finalData));
        //alert(JSON.stringify(finalData));
      }
    })
    event.preventDefault();
    $('#table1').attr('src', $('#table1').attr('src'));
    $('#dash-table').attr('src', $('#dash-table').attr('src'));
    // childWindow = "http://localhost:3050/table";

    // $.ajax({
    //   url : '/',
    //   type: 'GET',
    //   dataType: 'json',
    //   contentType:"application/json; charset=UTF-8",
    //   success: function (data) {
    //     console.log('from jquery get request');
    //     console.log(data);
    //     //$("p").text(JSON.stringify(finalData));
    //     //alert(JSON.stringify(finalData));
    //   }
    // })
    // dataTab.destroy();
    // dataTab.draw();
    // window.open('/add', "_blank");
  });

  $('#refresh').click(function(event){
    let newFilt = {'filters': []};
    $.ajax({
      url : '/',
      type: 'POST',
      dataType: 'json',
      data: JSON.stringify(newFilt),
      contentType:"application/json; charset=UTF-8",
      success: function (data) {
        console.log(JSON.stringify(newFilt))
        //$("p").text(JSON.stringify(finalData));
        //alert(JSON.stringify(finalData));
      }
    })
    $.ajax({
      url : '/table',
      type: 'POST',
      dataType: 'json',
      data: JSON.stringify(newFilt),
      contentType:"application/json; charset=UTF-8",
      success: function (data) {
        console.log(JSON.stringify(newFilt))
        //$("p").text(JSON.stringify(finalData));
        //alert(JSON.stringify(finalData));
      }
    })
    event.preventDefault();
    $('#table1').attr('src', $('#table1').attr('src'));
    $('#dash-table').attr('src', $('#dash-table').attr('src'));
    location.reload(true);
  });
  //
  // $('#export').click(function(event){
  //   $.ajax({
  //     url : '/export',
  //     type: 'GET',
  //     dataType: 'json',
  //     data: JSON.stringify(),
  //     contentType:"application/json; charset=UTF-8",
  //     success: function (data) {
  //       console.log("Export clicked")
  //       //$("p").text(JSON.stringify(finalData));
  //       //alert(JSON.stringify(finalData));
  //     }
  //   })
  //   event.preventDefault();
  //   window.open("/export", '_blank');
  // });


    // var rowID = -1;
    // var datatable = JSON.parse($("#table").attr("name"));
    // console.log("############################################")
    // console.log(datatable);
    // $('.dataframe').DataTable({
    // "scrollX": true,
    // "scrollY": 200,
    // "bFilter": false,
    // // "serverSide": true,
    // // "ajax": {
    // //   "url":  "/add",
    // //   "type": "GET",
    // //   "data": "data"},
    // "bSort": false,
    // "rowCallback": function( row, data ) {
    //   //this is needed temp for now because i do not have actual uncertainity data, removing this and having full data will fix the coloring
    //   if (rowID < 1){
    //     rowID++;
    //   }
    //   //get list of this rowID index and for all indicies in that list, color them.
    //   console.log("~~~~~~~~");
    //   console.log(datatable);
    //   console.log("~~~~~~~~~");
    //   console.log(datatable[rowID]);
    //   console.log("~~~~~~~~~");
    //   console.log(rowID);
    //   if (datatable.length >= 1 && datatable[0] != "%"){
    //     var rowIndicies = datatable[rowID]
    //     for (i of rowIndicies){
    //       console.log("COLORING THIS NUM: ")
    //       console.log(i);
    //       $('td', row).eq(i).addClass('highlight');
    //       rowIndicies.shift()
    //     }
    //   }
    //     }
    // });


  // var tabley = $('.dataframe').DataTable();
  // console.log(tabley.row(0).data().column(0).data());
  // console.log(tabley.column(0).data());
});
