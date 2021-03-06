function flattenize(data, is_staff) {

    let flatData = [];

    function FlatObj(datum, item, is_staff) {

        var format = d3.time.format('%Y-%m-%d');
        var has_items = item !== null;

        this.id = datum['alertID'];
        this.date = format(datum['date']);
        this.oblast = datum['oblast'];
        this.raion = datum['raion'];
        this.settlement = datum['settlement'];
        this.clusters = datum['clusters'].join('; ');
        if (is_staff) {
            this.partners = datum['partners'].join('; ');
        }
        this.needs = datum['needs'].join('; ');
        this.status = datum['status'];
        this.conflictRelated = datum['conflictRelated'];
        this.affected = datum['affected'];
        this.covered = datum['covered'];
        this.item = has_items ? item['item_name'] : '';
        this.quantity = has_items ? item['quantity_need'] : '';
        this.quantity_response = has_items ? datum['responses'][item['item_name']] : '';
        this.unit = has_items ? item["unit_name"] : '';
        this.latitude = datum['latitude'];
        this.longitude = datum['longitude'];
        this.view_url = datum['view_url'];
        this.beneficiaries_gap = (datum['covered'] ? datum['covered'] : 0) + ' / ' + datum['affected'];
        function items_gap() {
            var quantity = item['quantity_need'],
                response = datum['responses'][item['item_name']],
                unit = item["unit_name"];
            return (response ? response : 0) + ' / ' + quantity + ' ' + unit
        }

        this.items_gap = has_items ? items_gap() : '';
    }

    data.forEach(function (datum) {
        if (datum.items.length > 0) {
            datum.items.forEach(function (item) {
                flatData.push(new FlatObj(datum, item, is_staff));
            });
        } else {
            flatData.push(new FlatObj(datum, null, is_staff));
        }
    });

    return flatData

}


function FlatRow(datum, is_staff) {

    const format = d3.time.format('%Y-%m-%d');
    this.id = datum['alertID'];
    this.date = format(datum['date']);
    this.oblast = datum['oblast'];
    this.raion = datum['raion'];
    this.settlement = datum['settlement'];
    this.clusters = datum['clusters'].join('; ');
    if (is_staff) {
        this.partners = datum['partners'].join('; ');
    }
    this.needs = datum['needs'].join('; ');
    this.status = datum['status'];
    this.conflictRelated = datum['conflictRelated'];
    this.affected = datum['affected'];
    this.covered = datum['covered'];
    this.latitude = datum['latitude'];
    this.longitude = datum['longitude'];
    this.view_url = datum['view_url'];
    this.beneficiaries_gap = (datum['covered'] ? datum['covered'] : 0) + ' / ' + datum['affected'];
    this.items_gap = datum.items.map(function (item) {
                let item_name = item['item_name'],
                    quantity = item['quantity_need'],
                    response = datum['responses'][item_name],
                    unit = item['unit_name'];
                return item_name + ': ' + (response ? response : 0) + ' / ' + quantity + ' ' + unit
            });


}