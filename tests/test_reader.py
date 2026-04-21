from app.reader import read_videos


def test_read_videos(tmp_path):
    file = tmp_path / "test.csv"

    file.write_text(
        "title,ctr,retention_rate\n"
        "Video1,20,30\n"
        "Video2,25,35\n"
    )

    videos = read_videos(file)

    assert len(videos) == 2
    assert videos[0].title == "Video1"
    assert videos[1].ctr == 25.0