

$(document).ready(function(){
  var rowID = -1;
  var datatable = JSON.parse($("#table").attr("name"));
  console.log("############################################")
  console.log(datatable);
  $('.dataframe').DataTable({
  "scrollX": true,
  "scrollY": 200,
  "bFilter": false,
  "bSort": false,
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
      }
  });
  // var tabley = $('.dataframe').DataTable();
  // console.log(tabley.row(0).data().column(0).data());
  // console.log(tabley.column(0).data());
});
