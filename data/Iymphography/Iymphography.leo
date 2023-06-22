program dt.aleo {
	struct Inputs {
		p1: u32,
		p2: u32,
		p3: u32,
		p4: u32,
		p5: u32,
		p6: u32,
		p7: u32,
		p8: u32,
		p9: u32,
		p10: u32,
		p11: u32,
		p12: u32,
		p13: u32,
		p14: u32,
		p15: u32,
		p16: u32,
		p17: u32,
		p18: u32,
	}
	// Code auto generated from DecisionTreeClassifier using dt_to_leo_code.py 
	transition main(inputs: Inputs) -> public u32 {
		if (inputs.p18 < 3u32) {
			if (inputs.p2 < 2u32) {
				if (inputs.p6 < 2u32) {
					if (inputs.p13 < 4u32) {
						if (inputs.p18 < 2u32) {
							if (inputs.p1 < 2u32) {
								return 0u32;
							} else {
								if (inputs.p12 < 4u32) {
									return 1u32;
								} else {
									if (inputs.p13 < 3u32) {
										if (inputs.p9 < 2u32) {
											return 2u32;
										} else {
											return 1u32;
										}
									} else {
										return 1u32;
									}
								}
							}
						} else {
							if (inputs.p14 < 5u32) {
								if (inputs.p13 < 3u32) {
									return 1u32;
								} else {
									if (inputs.p8 < 2u32) {
										return 1u32;
									} else {
										return 2u32;
									}
								}
							} else {
								if (inputs.p12 < 4u32) {
									return 2u32;
								} else {
									return 1u32;
								}
							}
						}
					} else {
						return 2u32;
					}
				} else {
					if (inputs.p13 < 2u32) {
						return 0u32;
					} else {
						return 2u32;
					}
				}
			} else {
				if (inputs.p14 < 7u32) {
					return 1u32;
				} else {
					if (inputs.p13 < 4u32) {
						if (inputs.p13 < 3u32) {
							if (inputs.p10 < 3u32) {
								return 1u32;
							} else {
								return 2u32;
							}
						} else {
							return 1u32;
						}
					} else {
						return 2u32;
					}
				}
			}
		} else {
			if (inputs.p15 < 3u32) {
				if (inputs.p9 <= 2u32) {
					return 1u32;
				} else {
					return 3u32;
				}
			} else {
				if (inputs.p8 < 2u32) {
					if (inputs.p11 <= 2u32) {
						return 3u32;
					} else {
						return 1u32;
					}
				} else {
					if (inputs.p14 < 3u32) {
						if (inputs.p5 < 2u32) {
							return 2u32;
						} else {
							return 1u32;
						}
					} else {
						if (inputs.p1 < 3u32) {
							if (inputs.p13 < 3u32) {
								return 2u32;
							} else {
								if (inputs.p16 < 2u32) {
									return 1u32;
								} else {
									if (inputs.p3 < 2u32) {
										return 2u32;
									} else {
										if (inputs.p7 < 2u32) {
											return 1u32;
										} else {
											return 2u32;
										}
									}
								}
							}
						} else {
							return 2u32;
						}
					}
				}
			}
		}
	}
}