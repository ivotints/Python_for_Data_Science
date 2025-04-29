def ft_tqdm(lst: range) -> None:
    """
    A simple implementation of tqdm progress bar.

    Args:
        lst (range): A range object to iterate over

    Yields:
        Elements from the input range
    """
    total = len(lst)
    for i, item in enumerate(lst):
        progress = (i + 1) / total
        percentage = int(progress * 100)
        bar_length = 60
        num_blocks = int(progress * bar_length)
        bar = "=" * (num_blocks - 1) + ">" if num_blocks > 0 else ""
        bar = bar.ljust(bar_length)
        progress_text = f"{percentage:3}%|[{bar}]| {i+1}/{total}"
        print("\r" + progress_text, end="")
        yield item
