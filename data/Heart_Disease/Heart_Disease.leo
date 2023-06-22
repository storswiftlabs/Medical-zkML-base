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
	}
	// Code auto generated from DecisionTreeClassifier using dt_to_leo_code.py 
	transition main(inputs: Inputs) -> public u32 {
		if (inputs.p13 < 5u32) {
			if (inputs.p12 < 1u32) {
				if (inputs.p1 < 59u32) {
					if (inputs.p10 < 4u32) {
						if (inputs.p4 <= 109u32) {
							if (inputs.p10 < 1u32) {
								if (inputs.p8 < 160u32) {
									return 1u32;
								} else {
									return 0u32;
								}
							} else {
								return 0u32;
							}
						} else {
							return 0u32;
						}
					} else {
						return 1u32;
					}
				} else {
					if (inputs.p3 < 4u32) {
						if (inputs.p10 < 3u32) {
							if (inputs.p5 <= 302u32) {
								return 0u32;
							} else {
								if (inputs.p4 <= 150u32) {
									return 1u32;
								} else {
									return 0u32;
								}
							}
						} else {
							return 1u32;
						}
					} else {
						if (inputs.p1 < 64u32) {
							if (inputs.p2 < 1u32) {
								if (inputs.p5 <= 362u32) {
									return 1u32;
								} else {
									return 0u32;
								}
							} else {
								return 0u32;
							}
						} else {
							if (inputs.p2 < 1u32) {
								return 0u32;
							} else {
								return 2u32;
							}
						}
					}
				}
			} else {
				if (inputs.p3 < 4u32) {
					if (inputs.p1 < 56u32) {
						return 0u32;
					} else {
						if (inputs.p1 < 60u32) {
							if (inputs.p6 < 1u32) {
								return 1u32;
							} else {
								return 3u32;
							}
						} else {
							if (inputs.p2 < 1u32) {
								return 0u32;
							} else {
								if (inputs.p8 < 160u32) {
									return 2u32;
								} else {
									return 1u32;
								}
							}
						}
					}
				} else {
					if (inputs.p2 < 1u32) {
						if (inputs.p1 <= 63u32) {
							return 3u32;
						} else {
							return 0u32;
						}
					} else {
						if (inputs.p8 < 109u32) {
							return 3u32;
						} else {
							if (inputs.p4 <= 105u32) {
								return 3u32;
							} else {
								if (inputs.p5 <= 189u32) {
									return 4u32;
								} else {
									if (inputs.p10 < 1u32) {
										if (inputs.p8 < 157u32) {
											return 2u32;
										} else {
											if (inputs.p5 <= 267u32) {
												return 1u32;
											} else {
												return 4u32;
											}
										}
									} else {
										return 1u32;
									}
								}
							}
						}
					}
				}
			}
		} else {
			if (inputs.p12 < 1u32) {
				if (inputs.p1 < 52u32) {
					if (inputs.p5 < 294u32) {
						if (inputs.p10 < 3u32) {
							if (inputs.p3 < 4u32) {
								if (inputs.p4 <= 115u32) {
									return 1u32;
								} else {
									return 0u32;
								}
							} else {
								if (inputs.p1 <= 47u32) {
									return 1u32;
								} else {
									return 3u32;
								}
							}
						} else {
							if (inputs.p8 <= 163u32) {
								return 2u32;
							} else {
								return 4u32;
							}
						}
					} else {
						return 2u32;
					}
				} else {
					if (inputs.p9 < 1u32) {
						if (inputs.p4 <= 151u32) {
							return 0u32;
						} else {
							if (inputs.p10 < 1u32) {
								return 1u32;
							} else {
								if (inputs.p1 < 67u32) {
									return 0u32;
								} else {
									return 1u32;
								}
							}
						}
					} else {
						if (inputs.p4 < 148u32) {
							if (inputs.p5 < 241u32) {
								if (inputs.p10 < 3u32) {
									return 0u32;
								} else {
									if (inputs.p1 < 62u32) {
										return 1u32;
									} else {
										return 4u32;
									}
								}
							} else {
								return 1u32;
							}
						} else {
							return 3u32;
						}
					}
				}
			} else {
				if (inputs.p2 < 1u32) {
					if (inputs.p13 < 7u32) {
						return 2u32;
					} else {
						if (inputs.p12 < 3u32) {
							return 3u32;
						} else {
							if (inputs.p5 < 195u32) {
								return 3u32;
							} else {
								return 4u32;
							}
						}
					}
				} else {
					if (inputs.p1 < 59u32) {
						if (inputs.p7 < 1u32) {
							if (inputs.p10 < 2u32) {
								if (inputs.p10 < 2u32) {
									if (inputs.p5 <= 230u32) {
										if (inputs.p12 < 2u32) {
											return 0u32;
										} else {
											return 3u32;
										}
									} else {
										if (inputs.p5 < 314u32) {
											if (inputs.p1 < 58u32) {
												return 1u32;
											} else {
												return 2u32;
											}
										} else {
											return 3u32;
										}
									}
								} else {
									return 2u32;
								}
							} else {
								return 3u32;
							}
						} else {
							if (inputs.p4 <= 119u32) {
								return 4u32;
							} else {
								if (inputs.p4 <= 129u32) {
									return 1u32;
								} else {
									if (inputs.p4 <= 151u32) {
										if (inputs.p13 < 7u32) {
											if (inputs.p3 < 4u32) {
												return 2u32;
											} else {
												return 1u32;
											}
										} else {
											return 3u32;
										}
									} else {
										if (inputs.p3 <= 3u32) {
											return 1u32;
										} else {
											return 4u32;
										}
									}
								}
							}
						}
					} else {
						if (inputs.p4 < 133u32) {
							if (inputs.p5 <= 279u32) {
								if (inputs.p1 < 60u32) {
									return 2u32;
								} else {
									if (inputs.p3 < 4u32) {
										return 0u32;
									} else {
										if (inputs.p10 < 1u32) {
											return 0u32;
										} else {
											if (inputs.p10 < 4u32) {
												if (inputs.p4 < 128u32) {
													return 1u32;
												} else {
													if (inputs.p7 <= 1u32) {
														return 1u32;
													} else {
														return 2u32;
													}
												}
											} else {
												return 2u32;
											}
										}
									}
								}
							} else {
								return 3u32;
							}
						} else {
							if (inputs.p5 < 177u32) {
								return 3u32;
							} else {
								if (inputs.p8 < 140u32) {
									if (inputs.p1 < 65u32) {
										if (inputs.p11 < 2u32) {
											return 1u32;
										} else {
											return 4u32;
										}
									} else {
										return 2u32;
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
	}
}