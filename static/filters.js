var filters = [];
var finalData = {"filters": filters};

$(document).ready(function(){
  var firstLoad = true;
  var cols= JSON.parse($("#filters").attr("name"));
  console.log(cols);
  if (firstLoad){
    firstLoad = false;
    for(var i = 0; i < cols.length; i++) {
      $('#colNames select').append('<option value='+cols[i]+'>'+cols[i]+'</option>');
    }
  }
  var wrapperF = $(".filters");
  var wrapperDropdown = $(".dropdown");
  var filter_add = $(".addFilter");
  var f = 1;
  $(filter_add).click(function(e){
    //console.log("add desc clicked!");
    e.preventDefault();
    f++;
    var idee = "f" + f.toString();
    console.log("~~~~~???????????????~~~~~~~~~~~~~")
    console.log(cols)
    $(wrapperF).append('<div class="dropdown" id="colNames' + f.toString() + '"><input type="filterText0" class="add_field" name="filter0" id="e' + f.toString() +'"><select id="d' + f.toString() + '"></select><input type="filterText" class="add_field" name="filter" id=' + idee + '><a href="#" id=' + idee + ' class="remove_field">Remove</a></div>');
    var newSelector = "colNames" + f.toString() + " select"
    for(var i = 0; i < cols.length; i++) {
       $('#'+newSelector).append('<option value='+cols[i]+'>'+cols[i]+'</option>');
    }
    var idee1 = "e" + (f - 1).toString();
    var idee2 = "f" + (f - 1).toString();
    var idee3 = "d" + (f - 1).toString();
    //join the item as a big string to append to filters with colname, lower, upper
    var lower = $("#"+idee1).val();
    var upper = $("#"+idee2).val();
    var colFilter = $("#"+idee3).val();
    var finalFilterString =  colFilter + "," + lower + "," + upper;
    filters.push(finalFilterString);
    console.log("++++++++++++");
    console.log(filters);
    console.log("++++++++++++");
    //console.log(data);
  });

  $(wrapperF).on("click", ".remove_field", function(e){
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

  $('form').on('submit', function(event){
    $(this).target = "_blank";
    $.ajax({
      url : 'add',
      type: 'POST',
      dataType: 'json',
      data: JSON.stringify(finalData),
      contentType:"application/json; charset=UTF-8",
      success: function (data) {
        console.log(JSON.stringify(finalData))
        //$("p").text(JSON.stringify(finalData));
        //alert(JSON.stringify(finalData));
      }
    })
    event.preventDefault();
    window.open('/add', "_blank");
  });

  var rowID = -1;
  var datatable = JSON.parse($("#table").attr("name"));
  console.log(datatable);
  $('.dataframe').DataTable({
  "scrollX": true,
  "scrollY": 200,
  "bFilter": false,
  "rowCallback": function( row, data ) {
    //this is needed temp for now because i do not have actual uncertainity data, removing this and having full data will fix the coloring
    if (rowID < 1){
      rowID++;
    }
    //get list of this rowID index and for all indicies in that list, color them.
    console.log("~~~~~~~~");
    console.log(datatable);
    console.log("~~~~~~~~~");
    console.log(datatable[rowID]);
    console.log("~~~~~~~~~");
    console.log(rowID);
    if (datatable.length >= 1 && datatable[0] != "%"){
      var rowIndicies = datatable[rowID]
      for (i of rowIndicies){
        console.log("COLORING THIS NUM: ")
        console.log(i);
        $('td', row).eq(i).addClass('highlight');
        rowIndicies.shift()
      }
    }
      // if (datatable[index] == 1){
      //   console.log(index);
      //   var id = 0;
      //   if (index >= 30){
      //     id = Math.floor(index / (30 * rowID));
      //     console.log("before math");
      //     console.log(index);
      //     console.log("after math");
      //     console.log(id);
      //   }
        //$('td', row).eq(4).addClass('highlight');
      }
  });
  // var tabley = $('.dataframe').DataTable();
  // console.log(tabley.row(0).data().column(0).data());
  // console.log(tabley.column(0).data());
});
