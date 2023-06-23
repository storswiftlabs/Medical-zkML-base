program dt.aleo {
	struct Inputs {
		p1: u32,
		p2: u32,
		p3: u32,
		p4: u32,
		p5: u32,
		p6: u32,
	}
	// Code auto generated from DecisionTreeClassifier using dt_to_leo_code.py 
	transition main(inputs: Inputs) -> public u32 {
		if (inputs.p5 < 205u32) {
			if (inputs.p3 < 195u32) {
				if (inputs.p2 <= 770u32) {
					if (inputs.p5 < 75u32) {
						return 0u32;
					} else {
						if (inputs.p1 < 935u32) {
							if (inputs.p4 < 215u32) {
								return 1u32;
							} else {
								if (inputs.p2 < 535u32) {
									return 0u32;
								} else {
									if (inputs.p4 < 225u32) {
										return 0u32;
									} else {
										return 1u32;
									}
								}
							}
						} else {
							if (inputs.p1 <= 970u32) {
								return 0u32;
							} else {
								return 1u32;
							}
						}
					}
				} else {
					if (inputs.p1 < 895u32) {
						if (inputs.p5 < 95u32) {
							return 0u32;
						} else {
							return 1u32;
						}
					} else {
						if (inputs.p2 <= 1250u32) {
							return 0u32;
						} else {
							return 1u32;
						}
					}
				}
			} else {
				if (inputs.p4 < 215u32) {
					if (inputs.p1 < 935u32) {
						if (inputs.p1 < 855u32) {
							if (inputs.p4 < 145u32) {
								return 1u32;
							} else {
								return 0u32;
							}
						} else {
							return 0u32;
						}
					} else {
						if (inputs.p3 <= 250u32) {
							if (inputs.p2 <= 620u32) {
								return 1u32;
							} else {
								return 0u32;
							}
						} else {
							return 0u32;
						}
					}
				} else {
					if (inputs.p3 < 265u32) {
						if (inputs.p1 < 885u32) {
							if (inputs.p5 <= 80u32) {
								return 0u32;
							} else {
								return 1u32;
							}
						} else {
							if (inputs.p1 < 925u32) {
								if (inputs.p4 < 225u32) {
									return 1u32;
								} else {
									return 0u32;
								}
							} else {
								return 1u32;
							}
						}
					} else {
						if (inputs.p2 < 525u32) {
							if (inputs.p2 < 405u32) {
								return 0u32;
							} else {
								return 1u32;
							}
						} else {
							if (inputs.p4 < 325u32) {
								return 0u32;
							} else {
								if (inputs.p2 <= 1000u32) {
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
			if (inputs.p6 < 135u32) {
				if (inputs.p4 < 245u32) {
					if (inputs.p3 < 265u32) {
						if (inputs.p1 < 805u32) {
							return 0u32;
						} else {
							if (inputs.p1 <= 880u32) {
								return 1u32;
							} else {
								if (inputs.p2 < 795u32) {
									if (inputs.p6 < 55u32) {
										if (inputs.p1 < 915u32) {
											if (inputs.p1 < 905u32) {
												return 1u32;
											} else {
												if (inputs.p4 < 185u32) {
													return 1u32;
												} else {
													return 0u32;
												}
											}
										} else {
											return 1u32;
										}
									} else {
										if (inputs.p6 <= 70u32) {
											return 0u32;
										} else {
											if (inputs.p3 <= 240u32) {
												return 0u32;
											} else {
												return 1u32;
											}
										}
									}
								} else {
									if (inputs.p6 < 25u32) {
										return 0u32;
									} else {
										return 1u32;
									}
								}
							}
						}
					} else {
						if (inputs.p6 < 75u32) {
							if (inputs.p5 < 295u32) {
								if (inputs.p2 <= 570u32) {
									return 1u32;
								} else {
									if (inputs.p2 <= 830u32) {
										return 0u32;
									} else {
										if (inputs.p6 < 23u32) {
											return 0u32;
										} else {
											return 1u32;
										}
									}
								}
							} else {
								if (inputs.p3 < 585u32) {
									if (inputs.p5 <= 1250u32) {
										if (inputs.p2 < 695u32) {
											if (inputs.p6 <= 30u32) {
												if (inputs.p2 < 555u32) {
													return 1u32;
												} else {
													if (inputs.p3 <= 400u32) {
														return 0u32;
													} else {
														return 1u32;
													}
												}
											} else {
												return 1u32;
											}
										} else {
											return 1u32;
										}
									} else {
										return 0u32;
									}
								} else {
									return 0u32;
								}
							}
						} else {
							return 0u32;
						}
					}
				} else {
					if (inputs.p3 <= 390u32) {
						if (inputs.p2 <= 430u32) {
							if (inputs.p6 < 8u32) {
								return 1u32;
							} else {
								return 0u32;
							}
						} else {
							if (inputs.p5 <= 1190u32) {
								if (inputs.p4 < 285u32) {
									return 1u32;
								} else {
									if (inputs.p4 < 295u32) {
										if (inputs.p5 < 365u32) {
											return 0u32;
										} else {
											return 1u32;
										}
									} else {
										return 1u32;
									}
								}
							} else {
								if (inputs.p2 < 875u32) {
									return 1u32;
								} else {
									return 0u32;
								}
							}
						}
					} else {
						if (inputs.p4 < 425u32) {
							if (inputs.p1 <= 890u32) {
								if (inputs.p3 <= 460u32) {
									if (inputs.p5 < 935u32) {
										return 0u32;
									} else {
										return 1u32;
									}
								} else {
									return 1u32;
								}
							} else {
								if (inputs.p3 < 575u32) {
									if (inputs.p3 <= 520u32) {
										if (inputs.p1 < 925u32) {
											return 0u32;
										} else {
											if (inputs.p1 <= 960u32) {
												return 1u32;
											} else {
												return 0u32;
											}
										}
									} else {
										return 1u32;
									}
								} else {
									return 0u32;
								}
							}
						} else {
							if (inputs.p1 < 975u32) {
								return 1u32;
							} else {
								if (inputs.p4 <= 660u32) {
									return 0u32;
								} else {
									return 1u32;
								}
							}
						}
					}
				}
			} else {
				return 0u32;
			}
		}
	}
}