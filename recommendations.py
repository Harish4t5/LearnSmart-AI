
def generate_recommendation(topic, percentage, previous_percentage=None):

    # Calculate performance improvement
    improvement = None

    if previous_percentage is not None:
        improvement = percentage - previous_percentage

    # Determine learning level
    if percentage < 40:
        level = "Beginner"
        message = (
            f"You need to strengthen your understanding of {topic}. "
            "Start again with fundamental concepts."
        )
        practice = "Study basic concepts and solve beginner questions."

    elif percentage < 60:
        level = "Beginner"
        message = (
            f"You are developing your understanding of {topic}. "
            "Focus on your weak concepts."
        )
        practice = "Revise fundamentals and solve more beginner questions."

    elif percentage < 75:
        level = "Intermediate"
        message = (
            f"You have a fair understanding of {topic}. "
            "Improve your accuracy through regular practice."
        )
        practice = "Solve intermediate-level questions."

    else:
        level = "Advanced"
        message = (
            f"Excellent understanding of {topic}! "
            "Challenge yourself with advanced concepts."
        )
        practice = "Solve advanced problems."
        # Make recommendations responsive to performance trends
    if improvement is not None:

        if improvement <= -10:
            message = (
                f"Your performance in {topic} has dropped noticeably. "
                "Revise your mistakes before moving to harder concepts."
            )
            practice = (
                "Review incorrect answers, revise weak concepts, "
                "and retake a practice quiz."
            )

        elif improvement >= 10:
            message = (
                f"Great progress in {topic}! Your recent improvement "
                "shows that your understanding is getting stronger."
            )
            practice = (
                "Continue practising and gradually attempt "
                "more challenging questions."
            )
    # Add personalized progress feedback
    if improvement is not None:

        if improvement > 0:
            progress = (
                f"Your performance improved by {improvement:.2f} "
                "percentage points compared to your previous attempt."
            )

        elif improvement < 0:
            progress = (
                f"Your performance decreased by {abs(improvement):.2f} "
                "percentage points. Revise this topic carefully."
            )

        else:
            progress = "Your performance remained unchanged. Try a different practice approach."

    else:
        progress = "Complete another quiz to track your improvement."

    return {
        "topic": topic,
        "percentage": percentage,
        "previous_percentage": previous_percentage,
        "improvement": improvement,
        "level": level,
        "message": message,
        "practice": practice,
        "progress": progress
    }


if __name__ == "__main__":

    result = generate_recommendation(
    "Functions",
    65,
    previous_percentage=43.75
)

    print(result)
