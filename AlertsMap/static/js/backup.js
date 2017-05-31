var clusters = cf.clusterDim.groupAll().reduce(
    function (p, v) {
        v.clusters.forEach(function (val, idx) {
            p[val] = (p[val] || 0) + 1; //increment counts
        });
        return p;
    }
    , function (p, v) {
        v.clusters.forEach(function (val, idx) {
            p[val] = (p[val] || 0) - 1; //decrement counts
        });
        return p;

    }
    , function reduceInitial() {
        return {};
    }
).value();


clusters.all = function () {
    var newObject = [];
    for (var key in this) {
        if (this.hasOwnProperty(key) && key != "all") {
            newObject.push({
                key: key,
                value: this[key]
            });
        }
    }
    return newObject;
};


var partners = cf.partnerDim.groupAll().reduce(

    function (p, v) {
        v.partners.forEach(function (val, idx) {
            p[val] = (p[val] || 0) + 1; //increment counts
        });
        return p;
    }

    , function (p, v) {
        v.partners.forEach(function (val, idx) {
            p[val] = (p[val] || 0) - 1; //decrement counts
        });
        return p;

    }
    , function reduceInitial() {
        return {};
    }
).value();

partners.all = function () {
    var newObject = [];
    for (var key in this) {
        if (this.hasOwnProperty(key) && key != "all") {
            newObject.push({
                key: key,
                value: this[key]
            });
        }
    }
    return newObject;
};