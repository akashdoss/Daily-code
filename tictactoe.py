import streamlit as st

# Styling
st.set_page_config(page_title="Tic Tac Toe 🎮", layout="centered", page_icon="🎮")
st.markdown(
    """
    <style>
    body {
        background-color: #2c3e50;
        font-family: 'Arial', sans-serif;
    }
    h1, h2, h3 {
        color: #ecf0f1;
    }
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .grid {
        display: grid;
        grid-template-columns: repeat(3, 100px);
        gap: 10px;
    }
    .cell {
        width: 100px;
        height: 100px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 36px;
        font-weight: bold;
        border-radius: 10px;
        cursor: pointer;
        background-color: #34495e;
        color: #ecf0f1;
        transition: all 0.3s ease;
    }
    .cell:hover {
        background-color: #16a085;
        color: #fff;
    }
    .cell.disabled {
        cursor: not-allowed;
        background-color: #7f8c8d;
    }
    .winner {
        background-color: #27ae60 !important;
        color: #fff !important;
    }
    .draw {
        background-color: #f39c12 !important;
        color: #fff !important;
    }
    .button-container {
        margin-top: 20px;
    }
    .button {
        padding: 10px 20px;
        font-size: 18px;
        font-weight: bold;
        color: #2c3e50;
        background-color: #ecf0f1;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .button:hover {
        background-color: #bdc3c7;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def main():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.title("Tic Tac Toe 🎮")
    st.caption("Play the classic game with a modern touch!")

    # Initialize game state
    if "board" not in st.session_state:
        reset_game()

    # Handle game reset
    if st.button("Restart Game"):
        reset_game()

    # Display game board
    render_board()

    # Check for winner or draw
    winner = check_winner(st.session_state.board)
    if winner:
        display_winner(winner)

    st.markdown("</div>", unsafe_allow_html=True)


def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.current_turn = "X"
    st.session_state.winner = None


def render_board():
    board = st.session_state.board
    current_turn = st.session_state.current_turn

    def cell_callback(idx):
        if board[idx] == "" and not st.session_state.winner:
            board[idx] = current_turn
            st.session_state.current_turn = "O" if current_turn == "X" else "X"
            st.session_state.winner = check_winner(board)

    st.markdown("<div class='grid'>", unsafe_allow_html=True)
    for i in range(9):
        cell_class = "cell"
        if st.session_state.winner and i in st.session_state.winner.get("indices", []):
            cell_class += " winner"
        elif st.session_state.winner and st.session_state.winner["type"] == "draw":
            cell_class += " draw"

        disabled = "disabled" if board[i] or st.session_state.winner else ""
        content = board[i] or " "

        st.button(
            content,
            key=f"cell-{i}",
            on_click=cell_callback,
            args=(i,),
            disabled=bool(disabled),
        )
    st.markdown("</div>", unsafe_allow_html=True)


def check_winner(board):
    win_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] and board[a] != "":
            return {"type": "win", "player": board[a], "indices": [a, b, c]}
    if "" not in board:
        return {"type": "draw"}
    return None


def display_winner(winner):
    if winner["type"] == "win":
        st.subheader(f"🎉 Player {winner['player']} Wins! 🏆")
    elif winner["type"] == "draw":
        st.subheader("It's a Draw! 🤝")


if __name__ == "__main__":
    main()
