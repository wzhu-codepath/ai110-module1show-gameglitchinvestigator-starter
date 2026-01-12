from logic_utils import check_guess

#FIX: CoPilot helped add tests for check_guess function as well as add fixes to existing tests for tuple return type

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_check_guess_returns_tuple():
    # check_guess should return a tuple of (outcome, message)
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_numeric_comparison_high_low():
    # Test that numeric comparisons work correctly for high/low detection
    # Secret is 50
    secret = 50
    
    # Test values above the secret
    outcome_high, message_high = check_guess(75, secret)
    assert outcome_high == "Too High"
    assert message_high == "📉 Go LOWER!"
    
    # Test values below the secret
    outcome_low, message_low = check_guess(25, secret)
    assert outcome_low == "Too Low"
    assert message_low == "📈 Go HIGHER!"
