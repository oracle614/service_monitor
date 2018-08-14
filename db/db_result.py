from common.db_config import CONFIG
from common.utils import DB
from common.utils import DateFormat
mock_db = DB(CONFIG.ALIYUN_MOCK)
date_format = DateFormat()


class DBResult(object):
    def pass_update(self, product_id, tc_name, date):
        print('pass_update')
        passed_count = 1
        sql_get_count = 'select passed_count from service_product_result where product_id={} and date="{}" and tc_name = "{}";'.format(product_id, date, tc_name)
        print(sql_get_count)
        get_count = mock_db.query(sql_get_count)
        print(len(get_count))
        if len(get_count) ==0 :
            sql_pass = 'INSERT INTO service_product_result (product_id, tc_name, passed_count,failed_count,date) VALUES({}, "{}", "{}", 0, CURDATE())'.format(product_id, tc_name, passed_count)
            print(sql_pass)
            mock_db.update(sql_pass)
        else:
            passed_count = get_count[0]['passed_count']
            passed_count = passed_count + 1
            print(passed_count)
            sql_pass = 'UPDATE service_product_result set passed_count={} where product_id={} and date="{}" and tc_name="{}"; '.format(passed_count, product_id, date, tc_name)
            print(sql_pass)
            mock_db.update(sql_pass)
        sql_get_result = 'select result_id, tc_name, product_id, passed_count, failed_count from service_product_result where product_id={} and date="{}" and tc_name = "{}";'.format(product_id, date, tc_name)
        print(sql_get_result)
        result = mock_db.query(sql_get_result)
        print(result[0])
        return result[0]

    def fail_update(self, product_id, tc_name, date):
        failed_count = 1
        sql_get_count = 'select failed_count from service_product_result where product_id={} and date="{}" and tc_name = "{}";'.format(product_id, date, tc_name)
        get_count = mock_db.query(sql_get_count)
        if len(get_count) == 0:
            sql_fail = 'INSERT INTO service_product_result (product_id, tc_name, passed_count,failed_count,date) VALUES({}, "{}", 0, {}, CURDATE())'.format(product_id, tc_name, failed_count, )
            print(sql_fail)
            mock_db.update(sql_fail)
        else:
            failed_count = get_count[0]['failed_count']
            failed_count = failed_count + 1
            print(failed_count)
            sql_fail = 'UPDATE service_product_result set failed_count={} where product_id={} and date="{}" and tc_name="{}"; '.format(failed_count, product_id, date, tc_name)
            print(sql_fail)
            mock_db.update(sql_fail)
        sql_get_result = 'select result_id, tc_name, product_id, passed_count, failed_count from service_product_result where product_id={} and date="{}" and tc_name = "{}";'.format(product_id, date, tc_name)
        result = mock_db.query(sql_get_result)
        return result[0]

    def get_pass_count(self, product_id, tc_name, date):
        try:
            sql_get_count = 'select passed_count from service_product_result where product_id={} and date="{}" and tc_name = "{}";'.format(product_id, date, tc_name)
            print(sql_get_count)
            get_count = mock_db.query(sql_get_count)[0]['passed_count']
            return get_count
        except:
            return 0

    def get_fail_count(self, product_id, tc_name, date):
        try:
            sql_get_count = 'select failed_count from service_product_result where product_id={} and date="{}" and tc_name = "{}";'.format(product_id, date, tc_name)
            print(sql_get_count)
            get_count = mock_db.query(sql_get_count)[0]['failed_count']
            return get_count
        except:
            return 0


if __name__ == '__main__':
    result = DBResult()
    print(result.fail_update('1', 'test_tc_name', date_format.date_now()))
    # print(result.get_pass_count(1, date_format.date_now()))
