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
	}
	// Code auto generated from DecisionTreeClassifier using dt_to_leo_code.py 
	transition main(inputs: Inputs) -> public u32 {
		if (inputs.p12 < 675u32) {
			if (inputs.p3 < 1095u32) {
				if (inputs.p9 < 1345u32) {
					return 1u32;
				} else {
					return 0u32;
				}
			} else {
				if (inputs.p8 < 8u32) {
					if (inputs.p7 <= 3335000u32) {
						return 0u32;
					} else {
						return 1u32;
					}
				} else {
					if (inputs.p4 < 5u32) {
						return 1u32;
					} else {
						if (inputs.p3 < 1595u32) {
							if (inputs.p8 < 16u32) {
								return 0u32;
							} else {
								return 1u32;
							}
						} else {
							if (inputs.p3 < 17555u32) {
								return 1u32;
							} else {
								if (inputs.p3 <= 51790u32) {
									return 0u32;
								} else {
									return 1u32;
								}
							}
						}
					}
				}
			}
		} else {
			if (inputs.p5 < 275u32) {
				if (inputs.p12 < 785u32) {
					return 1u32;
				} else {
					if (inputs.p3 <= 1440u32) {
						return 0u32;
					} else {
						if (inputs.p7 <= 2725000u32) {
							if (inputs.p9 < 1385u32) {
								if (inputs.p8 < 10u32) {
									return 0u32;
								} else {
									if (inputs.p12 <= 950u32) {
										if (inputs.p3 < 2615u32) {
											return 1u32;
										} else {
											return 0u32;
										}
									} else {
										return 1u32;
									}
								}
							} else {
								return 0u32;
							}
						} else {
							if (inputs.p3 <= 12710u32) {
								return 0u32;
							} else {
								return 1u32;
							}
						}
					}
				}
			} else {
				if (inputs.p8 < 15u32) {
					if (inputs.p1 <= 790u32) {
						if (inputs.p7 <= 985000u32) {
							if (inputs.p9 <= 1410u32) {
								return 0u32;
							} else {
								return 1u32;
							}
						} else {
							if (inputs.p8 < 13u32) {
								return 0u32;
							} else {
								if (inputs.p12 < 935u32) {
									if (inputs.p2 < 5u32) {
										return 0u32;
									} else {
										return 1u32;
									}
								} else {
									return 0u32;
								}
							}
						}
					} else {
						if (inputs.p9 < 1355u32) {
							if (inputs.p2 < 5u32) {
								return 1u32;
							} else {
								return 0u32;
							}
						} else {
							return 0u32;
						}
					}
				} else {
					if (inputs.p1 <= 710u32) {
						if (inputs.p5 <= 650u32) {
							if (inputs.p5 < 325u32) {
								if (inputs.p1 <= 460u32) {
									return 0u32;
								} else {
									return 1u32;
								}
							} else {
								if (inputs.p8 < 36u32) {
									return 0u32;
								} else {
									if (inputs.p7 <= 2335000u32) {
										return 1u32;
									} else {
										return 0u32;
									}
								}
							}
						} else {
							return 1u32;
						}
					} else {
						if (inputs.p5 < 475u32) {
							return 1u32;
						} else {
							return 0u32;
						}
					}
				}
			}
		}
	}
}