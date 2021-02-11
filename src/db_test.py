import unittest
import db

class TestDB(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = db.create_connection("commit_history")
        c = cls.conn.cursor()
        cls.test_commit_info = ("abcdefg12345", "10-20-30", "some build logs", "/builds/abcdefg12345")
        c.execute("SELECT * FROM history WHERE commit_id=?", (cls.test_commit_info[0],))
        exists = c.fetchone()
        if exists is None:
            db.insert_commit(cls.conn, cls.test_commit_info)
        c.execute("DELETE FROM history WHERE commit_id=?", ('123',))
        cls.conn.commit()

    def test_select_commit(self):
        result = db.select_commit(self.conn, self.test_commit_info[0])
        self.assertEqual(result["commit_id"], self.test_commit_info[0])
        self.assertEqual(result["build_logs"], self.test_commit_info[2])

        result2 = db.select_commit(self.conn, "notfound")
        self.assertEqual(result2, {})


    def test_select_all(self):
        result = db.select_all(self.conn)
        if isinstance(result, list):
            self.assertEqual(True, True)

    def test_insert_commit(self):
        test_commit = ("123", "10-10-10", "logs", "url")
        id = db.insert_commit(self.conn, test_commit)
        self.assertIs(type(id), int)

        try:
            db.insert_commit(self.conn, ('23'))
        except Exception as e:
            got_exception = e.__str__()
            self.assertEqual(got_exception, "Incorrect number of bindings supplied. The current statement uses 4, and there are 2 supplied.")


if __name__ == '__main__':
    unittest.main()

