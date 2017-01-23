window.saveData = function() {
    var header = [
          'DATA_AS_OF'
        , 'CLUSTER_ID'
    ];

    var data = cf.dataasof.top(Infinity);

    data = data.map(function(record) {
        return [
              record['DATA_AS_OF']
            , record['CLUSTER_ID']
        ]
    });

    data.unshift(header);
    var res = d3.csv.formatRows(data);
    var blob = new Blob([res], {type: "text/csv;charset=utf-8"})
    saveAs(blob, 'ukraine-alerts-' + (new Date()).getTime() + '.csv')
};
