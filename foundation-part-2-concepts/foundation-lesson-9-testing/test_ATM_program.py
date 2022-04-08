from unittest import TestCase, main
from unittest.mock import patch
from ATM_program import verify_pin, log_in, run_atm


class TestVerifyPin(TestCase):

    # First attempt at writing a test, similar to the structure of those
    # we wrote in class.
    def test_verify_pin(self):
        expected = True
        result = verify_pin('1234')
        self.assertEqual(expected, result)

    # For this particular test, it can be done with less code using
    # assert.True
    def test_verify_pin_true(self):
        self.assertTrue(verify_pin('1234'))

    def test_verify_pin_false(self):
        self.assertFalse(verify_pin('3852'))


class TestLogIn(TestCase):

    # Need to mock the results of the pin input and the verify_pin() function
    # that are inside the log_in() function.
    @patch('ATM_program.input')
    @patch('ATM_program.verify_pin')
    def test_successful_log_in(self, mock_input, mock_verify_pin):
        mock_input.return_value = '1234'
        mock_verify_pin.return_value = True
        self.assertTrue(log_in())

    # Need to try multiple entries of pin to force an unsuccessful log in so
    # use side_effect rather than return_value
    @patch('ATM_program.input')
    def test_unsuccessful_log_in(self,  mock_input):
        mock_input.side_effect = ['2351', '5636', '3724', '3677']
        self.assertFalse(log_in())


class TestRunAtm(TestCase):

    # Mock verify_pin() and log_in() return values
    @patch('ATM_program.verify_pin')
    @patch('ATM_program.log_in')
    def test_successful_withdrawal(self, mock_verify_pin, mock_log_in):
        mock_verify_pin.return_value = True
        mock_log_in.return_value = True
        expected = 90
        result = run_atm(10)
        self.assertEqual(expected, result)

    @patch('ATM_program.verify_pin')
    @patch('ATM_program.log_in')
    def test_withdraw_too_much(self, mock_verify_pin, mock_log_in):
        mock_verify_pin.return_value = True
        mock_log_in.return_value = True
        with self.assertRaises(ValueError):
            run_atm(250)


if __name__ == '__main__':
    main()


# REFLECTION
# ----------

# 1. Should have used @patch.object rather than @patch as the objects being
#    patched within the function were directly imported as opposed to being
#    called from another module. See:
#    https://stackoverflow.com/questions/18191275/using-pythons-mock-patch-object-to-change-the-return-value-of-a-method-called-w

# 2. The order of the patch decorators matters. I have put them the wrong way
#    round. Decorators are evaluated from the bottom to the top. For example, in
#    test_successful_log_in() the verify_pin mock object was actually fed into
#    mock_input. I haven't figured out why it works both ways yet though!

# 3. Having said that, it was apparently wrong to mock the functions nested
#    within the one under test and I should have used:
#    @patch.object(ATM_program.log_in)
#    @patch.object(ATM_program.log_in)