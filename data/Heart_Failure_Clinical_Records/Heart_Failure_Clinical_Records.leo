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
		if (inputs.p12 < 735u32) {
			if (inputs.p8 < 9u32) {
				if (inputs.p12 < 705u32) {
					return 0u32;
				} else {
					return 1u32;
				}
			} else {
				if (inputs.p12 < 495u32) {
					if (inputs.p3 <= 20180u32) {
						if (inputs.p3 <= 560u32) {
							if (inputs.p3 < 495u32) {
								return 1u32;
							} else {
								return 0u32;
							}
						} else {
							if (inputs.p12 < 325u32) {
								return 1u32;
							} else {
								if (inputs.p3 < 1935u32) {
									return 0u32;
								} else {
									return 1u32;
								}
							}
						}
					} else {
						if (inputs.p4 < 5u32) {
							return 1u32;
						} else {
							return 0u32;
						}
					}
				} else {
					if (inputs.p5 <= 300u32) {
						return 1u32;
					} else {
						if (inputs.p3 <= 32320u32) {
							return 0u32;
						} else {
							return 1u32;
						}
					}
				}
			}
		} else {
			if (inputs.p8 < 16u32) {
				if (inputs.p1 <= 790u32) {
					if (inputs.p5 < 325u32) {
						if (inputs.p7 <= 3000000u32) {
							if (inputs.p8 < 12u32) {
								return 0u32;
							} else {
								if (inputs.p9 <= 1350u32) {
									return 0u32;
								} else {
									if (inputs.p5 < 275u32) {
										return 1u32;
									} else {
										return 0u32;
									}
								}
							}
						} else {
							if (inputs.p7 <= 3160000u32) {
								return 1u32;
							} else {
								if (inputs.p12 < 1795u32) {
									if (inputs.p12 <= 1070u32) {
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
						if (inputs.p8 < 7u32) {
							if (inputs.p10 < 5u32) {
								return 1u32;
							} else {
								return 0u32;
							}
						} else {
							if (inputs.p7 <= 900000u32) {
								if (inputs.p10 < 5u32) {
									return 1u32;
								} else {
									return 0u32;
								}
							} else {
								if (inputs.p1 < 695u32) {
									return 0u32;
								} else {
									if (inputs.p7 <= 3390000u32) {
										return 0u32;
									} else {
										if (inputs.p7 <= 4160000u32) {
											return 1u32;
										} else {
											return 0u32;
										}
									}
								}
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
				if (inputs.p12 <= 2100u32) {
					if (inputs.p3 < 625u32) {
						return 0u32;
					} else {
						if (inputs.p4 < 5u32) {
							if (inputs.p3 <= 840u32) {
								return 0u32;
							} else {
								if (inputs.p9 <= 1320u32) {
									if (inputs.p3 <= 4060u32) {
										return 1u32;
									} else {
										return 0u32;
									}
								} else {
									return 1u32;
								}
							}
						} else {
							if (inputs.p3 <= 1810u32) {
								return 1u32;
							} else {
								return 0u32;
							}
						}
					}
				} else {
					if (inputs.p3 < 8905u32) {
						return 0u32;
					} else {
						return 1u32;
					}
				}
			}
		}
	}
}