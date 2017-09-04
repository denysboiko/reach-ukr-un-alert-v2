function flattenize(data, is_staff) {

    var flatData = [];

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
        this.conflictRelated = (datum['conflictRelated'] == 1) ? gettext("Yes") : gettext('No');
        this.affected = datum['affected'];
        this.covered = datum['covered'];
        // this.context = datum['context'];
        // this.description = datum['description'];
        this.item = has_items ? item['item__item_name'] : '';
        this.quantity = has_items ? item['quantity_need'] : '';
        this.quantity_response = has_items ? datum['responses'][item['item__item_name']] : '';
        this.unit = has_items ? item["unit__unit_name"] : '';
        this.latitude = datum['latitude'];
        this.longitude = datum['longitude'];
        this.view_url = datum['view_url'];



        this.beneficiaries_gap = (datum['covered'] ? datum['covered'] : 0) + ' / ' + datum['affected'];

        function items_gap() {
            var quantity = item['quantity_need'],
                response = datum['responses'][item['item__item_name']],
                unit = item["unit__unit_name"];
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