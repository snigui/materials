

$(document).ready(function(){
  var rowID = -1;
  var datatable = JSON.parse($("#tableinframe").attr("name"));
  var now = new Date();
  var formatted = now.getHours() + "hr" + now.getMinutes() + "m" + now.getSeconds() + "s";
  console.log("############################################")
  console.log(datatable);
  $('.dataframe').DataTable({
    paging: true,
    pageLength: 4,
    dom: 'lBfrtip',
        buttons: [{
          extend: 'csv',
          text: 'Export',
          title: formatted
        }
      ],
  "scrollX": true,
  "sScrollY": 170,
  "bFilter": false,
  "bSort": true,
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
      while (rowIndicies.length != 0){
        console.log("COLORING THIS NUM: ")
        console.log(rowIndicies[0]);
        var i = rowIndicies[0];
        $('td', row).eq(i).addClass('highlight');
        rowIndicies.shift()
        console.log(rowIndicies);
      }
      }
    }
  });
  // var tabley = $('.dataframe').DataTable();
  // console.log(tabley.row(0).data().column(0).data());
  // console.log(tabley.column(0).data());
});
